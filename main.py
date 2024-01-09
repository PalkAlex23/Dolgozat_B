import csokiautomata
import sorozat
import baromfi_m

csokiautomata.csoki()
adatok = sorozat.sorozat()
sorozat.fajlba_kiir(sorozat.harommaloszthatoak_szama(adatok))
tarolt = baromfi_m.beolvas()
baromfi_m.vizsgalt(tarolt)
baromfi_m.kerekites(tarolt)
baromfi_m.nagyKacsa(tarolt)
