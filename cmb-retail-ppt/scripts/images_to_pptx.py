#!/usr/bin/env python3
"""Package full-slide images into a 16:9 PPTX without third-party libraries."""

from __future__ import annotations

import argparse
import mimetypes
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


SLIDE_W = 12192000
SLIDE_H = 6858000
SUPPORTED = {".png", ".jpg", ".jpeg"}


def natural_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def image_type(path: Path) -> tuple[str, str]:
    ext = ".jpg" if path.suffix.lower() == ".jpeg" else path.suffix.lower()
    if ext not in SUPPORTED:
        raise ValueError(f"Unsupported image type: {path.name}")
    content_type = mimetypes.types_map.get(ext, "image/png")
    return ext.lstrip("."), content_type


def slide_xml(slide_num: int, image_ext: str) -> str:
    name = f"slide-{slide_num:02d}.{image_ext}"
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="{SLIDE_W}" cy="{SLIDE_H}"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="{SLIDE_W}" cy="{SLIDE_H}"/>
        </a:xfrm>
      </p:grpSpPr>
      <p:pic>
        <p:nvPicPr>
          <p:cNvPr id="2" name="{escape(name)}"/>
          <p:cNvPicPr>
            <a:picLocks noChangeAspect="1"/>
          </p:cNvPicPr>
          <p:nvPr/>
        </p:nvPicPr>
        <p:blipFill>
          <a:blip r:embed="rId1"/>
          <a:stretch><a:fillRect/></a:stretch>
        </p:blipFill>
        <p:spPr>
          <a:xfrm>
            <a:off x="0" y="0"/>
            <a:ext cx="{SLIDE_W}" cy="{SLIDE_H}"/>
          </a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        </p:spPr>
      </p:pic>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>
'''


def slide_rels(media_name: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{escape(media_name)}"/>
</Relationships>
'''


def presentation_xml(count: int) -> str:
    slide_ids = "\n".join(
        f'    <p:sldId id="{256 + idx}" r:id="rId{idx}"/>' for idx in range(1, count + 1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldIdLst>
{slide_ids}
  </p:sldIdLst>
  <p:sldSz cx="{SLIDE_W}" cy="{SLIDE_H}" type="wide"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>
'''


def presentation_rels(count: int) -> str:
    rels = [
        f'  <Relationship Id="rId{idx}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{idx}.xml"/>'
        for idx in range(1, count + 1)
    ]
    rels.append(
        f'  <Relationship Id="rId{count + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>'
    )
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n' + "\n".join(rels) + "\n</Relationships>\n"


def content_types(images: list[Path]) -> str:
    defaults = {
        "rels": "application/vnd.openxmlformats-package.relationships+xml",
        "xml": "application/xml",
    }
    for image in images:
        ext, content_type = image_type(image)
        defaults[ext] = content_type

    default_xml = "\n".join(
        f'  <Default Extension="{escape(ext)}" ContentType="{escape(content_type)}"/>'
        for ext, content_type in sorted(defaults.items())
    )
    overrides = [
        '  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>',
        '  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
    ]
    overrides.extend(
        f'  <Override PartName="/ppt/slides/slide{idx}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for idx in range(1, len(images) + 1)
    )
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">\n' + default_xml + "\n" + "\n".join(overrides) + "\n</Types>\n"


def root_rels() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
'''


def app_xml(slide_count: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Codex</Application>
  <PresentationFormat>On-screen Show (16:9)</PresentationFormat>
  <Slides>{slide_count}</Slides>
</Properties>
'''


def core_xml() -> str:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>CMB Retail Finance Presentation</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>
'''


def theme_xml() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="CMB Retail">
  <a:themeElements>
    <a:clrScheme name="CMB Retail">
      <a:dk1><a:srgbClr val="000000"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="0B2A4A"/></a:dk2>
      <a:lt2><a:srgbClr val="F4F5F7"/></a:lt2>
      <a:accent1><a:srgbClr val="C8102E"/></a:accent1>
      <a:accent2><a:srgbClr val="0B2A4A"/></a:accent2>
      <a:accent3><a:srgbClr val="808080"/></a:accent3>
      <a:accent4><a:srgbClr val="D9D9D9"/></a:accent4>
      <a:accent5><a:srgbClr val="B00020"/></a:accent5>
      <a:accent6><a:srgbClr val="333333"/></a:accent6>
      <a:hlink><a:srgbClr val="0563C1"/></a:hlink>
      <a:folHlink><a:srgbClr val="954F72"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="CMB Fonts">
      <a:majorFont><a:latin typeface="Arial"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Arial"/></a:majorFont>
      <a:minorFont><a:latin typeface="Arial"/><a:ea typeface="Microsoft YaHei"/><a:cs typeface="Arial"/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="CMB Format">
      <a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>
      <a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>
      <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
      <a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
</a:theme>
'''


def build_pptx(images: list[Path], output: Path) -> None:
    if not images:
        raise ValueError("No images found.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types(images))
        zf.writestr("_rels/.rels", root_rels())
        zf.writestr("docProps/app.xml", app_xml(len(images)))
        zf.writestr("docProps/core.xml", core_xml())
        zf.writestr("ppt/presentation.xml", presentation_xml(len(images)))
        zf.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(len(images)))
        zf.writestr("ppt/theme/theme1.xml", theme_xml())
        for idx, image in enumerate(images, start=1):
            ext, _ = image_type(image)
            media_name = f"image{idx}.{ext}"
            zf.write(image, f"ppt/media/{media_name}")
            zf.writestr(f"ppt/slides/slide{idx}.xml", slide_xml(idx, ext))
            zf.writestr(f"ppt/slides/_rels/slide{idx}.xml.rels", slide_rels(media_name))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a 16:9 PPTX from full-slide images.")
    parser.add_argument("--images-dir", required=True, type=Path, help="Directory containing slide images.")
    parser.add_argument("--output", required=True, type=Path, help="Output .pptx path.")
    args = parser.parse_args()

    images = sorted(
        [path for path in args.images_dir.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED],
        key=natural_key,
    )
    try:
        build_pptx(images, args.output)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"created {args.output} with {len(images)} slides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
