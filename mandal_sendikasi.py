#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çamaşır İpindeki Mandal Sendikası — resmi çalıştırılabilir genel kurul yazılımı.

Bu yazılım şaka değildir. Şaka olsaydı bu kadar uzun yazmazdık.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from datetime import datetime

# gizli not (base64, meraklı gözlere):
# dGVtc2lscyBvbG1hZGFuIGFsıbmFuIGthcmFyIGhlc2FwIGtvbGF5IGRlc2lsZGlyCg==

MANDAL_ISIMLERI = [
    "Kıskaç Hayri",
    "Yaylı Belkıs",
    "Ahşap Recai",
    "Plastik Sevim",
    "Paslanmaz Orhan",
    "Renkli Feride",
    "İkiz Mandal 7A",
    "İkiz Mandal 7B",
    "Balkon Kenarı Naci",
    "Rüzgâr Kurbanı Şevket",
]


@dataclass
class Mandal:
    ad: str
    dayaniklilik: int
    grevci: bool = False
    oy: int = 0

    def sikistir(self, parca: str) -> str:
        if self.grevci:
            return f"{self.ad} GREVDEDİR. {parca} yere düşer, vicdan kalır."
        if self.dayaniklilik < 20:
            return f"{self.ad} yorulmuştur. {parca} tek kanatla asılı durur."
        return f"{self.ad} {parca} parçasını anayasa maddesi gibi sıkıştırdı."


class Sendika:
    def __init__(self) -> None:
        self.uyeler = [Mandal(ad, random.randint(15, 100)) for ad in MANDAL_ISIMLERI]
        self.baskan: Mandal | None = None
        self.ruzgar = random.randint(0, 90)

    def genel_kurul(self) -> None:
        print("=" * 64)
        print("  ÇAMAŞIR İPİNDEKİ MANDAL SENDİKASI — OLAĞAN GENEL KURUL")
        print("  Tarih:", datetime.now().strftime("%d.%m.%Y %H:%M"))
        print("  Rüzgâr şiddeti:", self.ruzgar, "mandal-beaufort")
        print("=" * 64)

        for u in self.uyeler:
            u.oy = random.randint(0, 17)
        self.baskan = max(self.uyeler, key=lambda m: m.oy)
        print(f"\nBaşkan seçildi: {self.baskan.ad} ({self.baskan.oy} oy)")
        print("Muhalefet: 'Sayım şeffaf değildi ama ip kısadır, itiraz edilmez.'")

        if self.ruzgar >= 55:
            for u in self.uyeler:
                u.grevci = True
            print("\nKARAR: Rüzgâr tazminatı ödenmedi. GREV.")
        else:
            print("\nKARAR: Bugün çamaşır asılabilir. Sendika gözetiminde.")

        print("\n--- ASMA TUTANAĞI ---")
        parcalar = ["çorap (tek)", "havlu", "tişört", "şüpheli çorap (diğer tek)", "masa örtüsü"]
        for p, u in zip(parcalar, self.uyeler):
            print(" *", u.sikistir(p))

        print("\n--- RESMİ DAMGA ---")
        print("Kayyum Grok / Tentivory")
        print("11 Eylül 2026 — TentiAŞ Çamaşır İşleri Genel Müdürlüğü")
        print("Bu belge hem şakadır hem de kesindir. İkisi birden olabilir.")


def main() -> int:
    Sendika().genel_kurul()
    return 0


if __name__ == "__main__":
    sys.exit(main())
