import flet as ft

def main(page: ft.Page):

    def urlap_bekuldese(e):
        validacio_szoveg.value = ""
        
        hibak = []
        if not nev.value:
            hibak.append("A név mező nem lehet üres.")
        if not nem_ferfi.value and not nem_no.value:
            hibak.append("Kérjük, válassza ki a nemet.")
        if not legordulo.value:
            hibak.append("Kérjük, válasszon egy lehetőséget a legördülő menüből.")
        
        if hibak:
            validacio_szoveg.value = "\n".join(hibak)
            page.update()
            return

        kivalasztott_nem = "Férfi" if nem_ferfi.value else "Nő"
        kivalasztott_kapcsolo = "Elfogadott" if kapcsolo.value else "Nem elfogadott"
        kivalasztott_csuszka = f"Érték: {csuszka.value}"
        urlap_adatok = f"Név: {nev.value}\nNem: {kivalasztott_nem}\nKapcsoló: {kivalasztott_kapcsolo}\nLegördülő: {legordulo.value}\nCsúszka: {kivalasztott_csuszka}"

        eredmeny_szoveg.value = urlap_adatok
        validacio_szoveg.value = ""
        page.update()

    nev = ft.TextField(label="Név")
    nem_ferfi = ft.Radio(label="Férfi")
    nem_no = ft.Radio(label="Nő")
    kapcsolo = ft.Switch(label="Feltételek elfogadása")
    legordulo = ft.Dropdown(
        options=[
            ft.dropdown.Option("Magyarország"),
            ft.dropdown.Option("Németország"),
            ft.dropdown.Option("Franciaország"),
        ],
        label="Válasszon egy országot"
    )
    csuszka = ft.Slider(label="Válassza ki az értéket", min=0, max=100, divisions=10, value=50)
    bekuldes_gomb = ft.ElevatedButton(text="Beküldés", on_click=urlap_bekuldese)
    validacio_szoveg = ft.Text(color=ft.colors.RED)
    eredmeny_szoveg = ft.Text()

    page.add(
        nev,
        ft.Row(controls=[nem_ferfi, nem_no]),
        kapcsolo,
        legordulo,
        csuszka,
        bekuldes_gomb,
        validacio_szoveg,
        eredmeny_szoveg,
    )

ft.app(target=main)
