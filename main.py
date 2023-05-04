import requests
import urllib.request
import os

# получения 1 списка категорий
req1 = requests.get('https://apicr.minzdrav.gov.ru/api.ashx?op=GetMkbTreeItem&age=1&id=0&query=')
categories_level_1 = req1.json()['items']


def get_category(category_id):
    return requests.get(
        f'https://apicr.minzdrav.gov.ru/api.ashx?op=GetMkbTreeItem&age=1&id={category_id}&query='
    )


def get_pdf(code, path):
    urllib.request.urlretrieve(
        f'https://apicr.minzdrav.gov.ru/api.ashx?op=GetClinrecPdf&id={code}',
        path
    )
    print(f'Скачан файл: {path}')


# получения 2 списка категорий
for category_level_1 in categories_level_1:
    categories_level_2 = get_category(category_level_1["id"]).json()['items']
    if not os.path.exists(
            f'{category_level_1["code"]}'
    ):
        os.mkdir(
            f'{category_level_1["code"]}'
        )
    # получения 3 списка категорий
    for category_level_2 in categories_level_2:
        req3 = get_category(category_level_2["id"])
        if not os.path.exists(
                f'{category_level_1["code"]}/{category_level_2["code"]}'
        ):
            os.mkdir(
                f'{category_level_1["code"]}/{category_level_2["code"]}'
            )

        if len(req3.json()['items']) == 0:
            path = (
                f'{category_level_1["code"]}/{category_level_2["code"]}'
                f'/KP{req3.json()["clinrecs"][0]["id"]}.pdf'
            )
            get_pdf(req3.json()["clinrecs"][0]["id"], path)
        else:
            categories_level_3 = req3.json()['items']
            # получения 4 списка категорий
            for category_level_3 in categories_level_3:
                req4 = get_category(category_level_3["id"])
                if not os.path.exists(
                        f'{category_level_1["code"]}/{category_level_2["code"]}/{category_level_3["code"]}'
                ):
                    os.mkdir(
                        f'{category_level_1["code"]}/{category_level_2["code"]}/{category_level_3["code"]}'
                    )
                if len(req4.json()['items']) == 0:
                    if len(req4.json()['clinrecs']) > 1:
                        for item4 in req4.json()['clinrecs']:
                            path = (
                                f'{category_level_1["code"]}/{category_level_2["code"]}'
                                f'/{category_level_3["code"]}/KP{item4["id"]}.pdf'
                            )
                            get_pdf(item4["id"], path)
                    else:
                        path = (
                            f'{category_level_1["code"]}/{category_level_2["code"]}'
                            f'/{category_level_3["code"]}/KP{req4.json()["clinrecs"][0]["id"]}.pdf'
                        )
                        get_pdf(req4.json()["clinrecs"][0]["id"], path)
                else:
                    categories_level_4 = req4.json()['items']

                    # получения 5 списка категорий
                    for category_level_4 in categories_level_4:
                        req5 = get_category(category_level_4["id"])

                        if not os.path.exists(
                                f'{category_level_1["code"]}'
                                f'/{category_level_2["code"]}/{category_level_3["code"]}'
                        ):
                            os.mkdir(
                                f'{category_level_1["code"]}'
                                f'/{category_level_2["code"]}/{category_level_3["code"]}'
                            )
                        if not os.path.exists(
                                f'{category_level_1["code"]}/{category_level_2["code"]}'
                                f'/{category_level_3["code"]}/{category_level_4["code"]}'
                        ):
                            os.mkdir(
                                f'{category_level_1["code"]}/{category_level_2["code"]}'
                                f'/{category_level_3["code"]}/{category_level_4["code"]}'
                            )

                        if len(req5.json()['items']) == 0:
                            if len(req5.json()['clinrecs']) > 1:
                                for item5 in req5.json()['clinrecs']:
                                    path = (
                                        f'{category_level_1["code"]}/{category_level_2["code"]}'
                                        f'/{category_level_3["code"]}/{category_level_4["code"]}'
                                        f'/KP{item5["id"]}.pdf'
                                    )
                                    get_pdf(item5["id"], path)
                            else:
                                path = (
                                    f'{category_level_1["code"]}/{category_level_2["code"]}'
                                    f'/{category_level_3["code"]}/{category_level_4["code"]}'
                                    f'/KP{req5.json()["clinrecs"][0]["id"]}.pdf'
                                )
                                get_pdf(req5.json()["clinrecs"][0]["id"], path)
                        else:
                            categories_level_5 = req5.json()['items']

                            # получения 6 списка категорий
                            for category_level_5 in categories_level_5:
                                req6 = get_category(category_level_5["id"])

                                if not os.path.exists(
                                        f'{category_level_1["code"]}/{category_level_2["code"]}'
                                        f'/{category_level_3["code"]}/{category_level_4["code"]}'
                                        f'/{category_level_5["code"]}'
                                ):
                                    os.mkdir(
                                        f'{category_level_1["code"]}/{category_level_2["code"]}'
                                        f'/{category_level_3["code"]}/{category_level_4["code"]}'
                                        f'/{category_level_5["code"]}'
                                    )

                                if len(req6.json()['items']) == 0:
                                    if len(req6.json()['clinrecs']) > 1:
                                        for item6 in req6.json()['clinrecs']:
                                            path = (
                                                f'{category_level_1["code"]}/{category_level_2["code"]}'
                                                f'/{category_level_3["code"]}/{category_level_4["code"]}'
                                                f'/{category_level_5["code"]}/KP{item6["id"]}.pdf'
                                            )
                                            get_pdf(item6["id"], path)
                                    else:
                                        path = (
                                            f'{category_level_1["code"]}/{category_level_2["code"]}'
                                            f'/{category_level_3["code"]}/{category_level_4["code"]}'
                                            f'/{category_level_5["code"]}/KP{req6.json()["clinrecs"][0]["id"]}.pdf'
                                        )
                                        get_pdf(req6.json()["clinrecs"][0]["id"], path)
