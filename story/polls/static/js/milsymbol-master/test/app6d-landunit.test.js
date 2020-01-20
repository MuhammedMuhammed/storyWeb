import { ms } from "../src/milsymbol";
ms.reset();
import { app6d } from "stanagapp6";
import verify from "./number-sidc";
ms.setStandard("APP6");

import { landunit as icons } from "../src/numbersidc";
ms.addIcons(icons);

export default verify(ms, app6d["10"]);
