import flet as ft
import requests as re

def main(page: ft.page):
    page.bgcolor = ft.colors.WHITE24
    page.window_width = 380
    page.window_height = 480
    page.title = 'Flet Requests'

    textFiel = ft.TextField()

    def req(e):
        reqLink = textFiel.value
        conectionBool = False
        try:
            REQ = re.get(reqLink)
            conectionBool = True
        except:
            pass

        try:
            reasonRes = REQ.reason
        except:
            reasonRes = 'None'

        try:
            jsonRes = REQ.json()
        except:
            jsonRes = 'None'

        if conectionBool:
            conection.value = REQ
        else:
            conection.value = 'None'
        reason.value = reasonRes
        json.value = jsonRes

        conection.update()
        reason.update()
        json.update()


    botaoRequest = ft.TextButton(text='Request', on_click=req)

    labelConection = ft.Text(value='Conection:')
    conection = ft.Text(value='None')

    espaco1 = ft.Text(value='', color=ft.colors.WHITE24)

    labelReason = ft.Text(value='Reason:')
    reason = ft.Text(value='None')

    espaco2 = ft.Text(value='', color=ft.colors.WHITE24)

    labelJson = ft.Text(value='JSon:')
    json = ft.Text(value='None')

    page.add(textFiel, botaoRequest, labelConection, conection, espaco1, labelReason, reason, espaco2, labelJson, json)

if __name__ == '__main__':
    ft.app(target=main)