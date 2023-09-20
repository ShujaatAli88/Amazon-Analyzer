import requests

def followings(user_id):
    cookies = {
        'session-id': '131-0213689-2063762',
        'sp-cdn': '"L5Z9:PK"',
        'ubid-main': '131-5842464-5946415',
        'x-main': '"2X?zoebw84DaY0Q301zfFDDflVhiGYLdPFuPi4Gst?u5TdejNhgvt5c5se6bf6W@"',
        'at-main': 'Atza|IwEBIOA4ucmS27lGBX9JqLT8MZMPhIydaKlgT77gvL-5BygrRNCeSeJn7cflJS_AOCCmZsBOoDiupjo7j7QMFJR0fdohAO_D8sM6DzMFp8DXVkBLEMor3DMFJhsytoGLL43ulMpcRip5OKSXVv2Rc8ZFAUiey3vbRZAqi1f9KrDdcBCKRYQ6nyk_95sTA_7U8JWCrThsYvqqqy8BPNRmoQRUzrnFY3finSC-ZS5MucgVUVVFNA',
        'sess-at-main': '"oWkmFySL3Xn1jZ+/MrhNDzAYeqy35bBAVRKf/NUF2aA="',
        'sst-main': 'Sst1|PQE48cvsPuFqYcSgTtYkKOWRCWA1-dwmYPOr-sEMxQytNjW_JM9Eo7E9dkK8T9QFBkwNf4MifEhb4vm-j5eXWJzHA9_WJ_GQ-4TS-AngRuhU2AjLOYubeffK8hbpUCH-ab6S8o43mGjesmgi44h2O5vrLWFKbwts23hC7MUyqi7AyGHgRF7gJBmn39-EJwSrK1U3S01dS3fdYHO5_fqJq-D2yBoV6Rc-WWJr4r-fkxHlFsJLSzRhJknSS9fn0S4jg52C6nDBHb-8CQdk3Vbh-ifeVjJrryt7vY8FnFpQnM5gnfI',
        'lc-main': 'en_US',
        'session-id-time': '2082787201l',
        'i18n-prefs': 'USD',
        'ld': 'AZUSSOA-sell',
        's_pers': '%20s_fid%3D1D9241E4A786C0DB-342FC1ADB15D3CB4%7C1852886031145%3B%20s_dl%3D1%7C1695035031145%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1695035031146%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271695033231150%2527%255D%255D%7C1852886031150%3B',
        'skin': 'noskin',
        'av-profile': 'cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTNJSTdSVEpDUDIyMDEmdGltZXN0YW1wPTE2OTUxMTA1NTk0MDUmdmVyc2lvbj12MQ.g7mZ4c4VZzuwzXBZEDZzoleHdSGwySI5Y8WW6pBfUWcwAAAAAQAAAABlCVWfcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ',
        'av-timezone': 'America/Los_Angeles',
        's_cc': 'true',
        's_nr': '1695111033104-New',
        's_vnum': '2127111033104%26vn%3D1',
        's_dslv': '1695111033104',
        's_sq': '%5B%5BB%5D%5D',
        's_ppv': '40',
        'session-token': '5ll+K6fHu0s44sfMMgUIJ2Nr7Q7MxNl25zVirLg3IGia780gaKCYviO8hbf10GVVSoHoNr9zZt5sbq1Q0GKVdUkZAkVb8sfxdPLPbbmzcwhdoD3vb9MGDeffc/+tiY2wb2u8Zw51GmewbgOAz7WF44vMAJiuoNiDQh/KPj2t5TWVOneI/L039hcAWgTQ+mfn1JvfHUr1PCu/Ax0rY2tPeyeEJt9Pp9qa2OBcH1P6TJ7jsDNK6p0xgwJ2ewhmIxovbLo/J2lGYuEckzi+4bQtVBlcTNspiTijQ3onNCWrBBKD8XpWORJ8XkX1R8RcELAAeS7/4msmTw5TCx9h8HGMz4yartio55Cj6Be0iITaU6dMHGT82oUvDjj2GwAUhhW/',
        'csm-hit': 'tb:s-AYR8CRTC44FR0TXWRWZW|1695116762754&t:1695116763140&adb:adblk_no',
    }
    
    headers = {
        'authority': 'www.amazon.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'session-id=131-0213689-2063762; sp-cdn="L5Z9:PK"; ubid-main=131-5842464-5946415; x-main="2X?zoebw84DaY0Q301zfFDDflVhiGYLdPFuPi4Gst?u5TdejNhgvt5c5se6bf6W@"; at-main=Atza|IwEBIOA4ucmS27lGBX9JqLT8MZMPhIydaKlgT77gvL-5BygrRNCeSeJn7cflJS_AOCCmZsBOoDiupjo7j7QMFJR0fdohAO_D8sM6DzMFp8DXVkBLEMor3DMFJhsytoGLL43ulMpcRip5OKSXVv2Rc8ZFAUiey3vbRZAqi1f9KrDdcBCKRYQ6nyk_95sTA_7U8JWCrThsYvqqqy8BPNRmoQRUzrnFY3finSC-ZS5MucgVUVVFNA; sess-at-main="oWkmFySL3Xn1jZ+/MrhNDzAYeqy35bBAVRKf/NUF2aA="; sst-main=Sst1|PQE48cvsPuFqYcSgTtYkKOWRCWA1-dwmYPOr-sEMxQytNjW_JM9Eo7E9dkK8T9QFBkwNf4MifEhb4vm-j5eXWJzHA9_WJ_GQ-4TS-AngRuhU2AjLOYubeffK8hbpUCH-ab6S8o43mGjesmgi44h2O5vrLWFKbwts23hC7MUyqi7AyGHgRF7gJBmn39-EJwSrK1U3S01dS3fdYHO5_fqJq-D2yBoV6Rc-WWJr4r-fkxHlFsJLSzRhJknSS9fn0S4jg52C6nDBHb-8CQdk3Vbh-ifeVjJrryt7vY8FnFpQnM5gnfI; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; ld=AZUSSOA-sell; s_pers=%20s_fid%3D1D9241E4A786C0DB-342FC1ADB15D3CB4%7C1852886031145%3B%20s_dl%3D1%7C1695035031145%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1695035031146%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271695033231150%2527%255D%255D%7C1852886031150%3B; skin=noskin; av-profile=cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTNJSTdSVEpDUDIyMDEmdGltZXN0YW1wPTE2OTUxMTA1NTk0MDUmdmVyc2lvbj12MQ.g7mZ4c4VZzuwzXBZEDZzoleHdSGwySI5Y8WW6pBfUWcwAAAAAQAAAABlCVWfcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ; av-timezone=America/Los_Angeles; s_cc=true; s_nr=1695111033104-New; s_vnum=2127111033104%26vn%3D1; s_dslv=1695111033104; s_sq=%5B%5BB%5D%5D; s_ppv=40; session-token=5ll+K6fHu0s44sfMMgUIJ2Nr7Q7MxNl25zVirLg3IGia780gaKCYviO8hbf10GVVSoHoNr9zZt5sbq1Q0GKVdUkZAkVb8sfxdPLPbbmzcwhdoD3vb9MGDeffc/+tiY2wb2u8Zw51GmewbgOAz7WF44vMAJiuoNiDQh/KPj2t5TWVOneI/L039hcAWgTQ+mfn1JvfHUr1PCu/Ax0rY2tPeyeEJt9Pp9qa2OBcH1P6TJ7jsDNK6p0xgwJ2ewhmIxovbLo/J2lGYuEckzi+4bQtVBlcTNspiTijQ3onNCWrBBKD8XpWORJ8XkX1R8RcELAAeS7/4msmTw5TCx9h8HGMz4yartio55Cj6Be0iITaU6dMHGT82oUvDjj2GwAUhhW/; csm-hit=tb:s-AYR8CRTC44FR0TXWRWZW|1695116762754&t:1695116763140&adb:adblk_no',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.amazon.com/gp/profile/amzn1.account.AFV2KSFLWI3OUOVJMMA5Y3XOEFKA/ref=cm_cr_dp_d_gw_tr?ie=UTF8',
        'rtt': '0',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '1920',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '1920',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    params = {
        'preview': 'false',
    }
    
    response = requests.get(
        'https://www.amazon.com/hz/follow/ajax/amzn1.account.'+user_id+'/getFollowingWidget',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response


def hearts(user):
    cookies = {
        'session-id': '131-0213689-2063762',
        'sp-cdn': '"L5Z9:PK"',
        'ubid-main': '131-5842464-5946415',
        'x-main': '"2X?zoebw84DaY0Q301zfFDDflVhiGYLdPFuPi4Gst?u5TdejNhgvt5c5se6bf6W@"',
        'at-main': 'Atza|IwEBIOA4ucmS27lGBX9JqLT8MZMPhIydaKlgT77gvL-5BygrRNCeSeJn7cflJS_AOCCmZsBOoDiupjo7j7QMFJR0fdohAO_D8sM6DzMFp8DXVkBLEMor3DMFJhsytoGLL43ulMpcRip5OKSXVv2Rc8ZFAUiey3vbRZAqi1f9KrDdcBCKRYQ6nyk_95sTA_7U8JWCrThsYvqqqy8BPNRmoQRUzrnFY3finSC-ZS5MucgVUVVFNA',
        'sess-at-main': '"oWkmFySL3Xn1jZ+/MrhNDzAYeqy35bBAVRKf/NUF2aA="',
        'sst-main': 'Sst1|PQE48cvsPuFqYcSgTtYkKOWRCWA1-dwmYPOr-sEMxQytNjW_JM9Eo7E9dkK8T9QFBkwNf4MifEhb4vm-j5eXWJzHA9_WJ_GQ-4TS-AngRuhU2AjLOYubeffK8hbpUCH-ab6S8o43mGjesmgi44h2O5vrLWFKbwts23hC7MUyqi7AyGHgRF7gJBmn39-EJwSrK1U3S01dS3fdYHO5_fqJq-D2yBoV6Rc-WWJr4r-fkxHlFsJLSzRhJknSS9fn0S4jg52C6nDBHb-8CQdk3Vbh-ifeVjJrryt7vY8FnFpQnM5gnfI',
        'lc-main': 'en_US',
        'session-id-time': '2082787201l',
        'i18n-prefs': 'USD',
        'ld': 'AZUSSOA-sell',
        's_pers': '%20s_fid%3D1D9241E4A786C0DB-342FC1ADB15D3CB4%7C1852886031145%3B%20s_dl%3D1%7C1695035031145%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1695035031146%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271695033231150%2527%255D%255D%7C1852886031150%3B',
        'skin': 'noskin',
        'av-profile': 'cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTNJSTdSVEpDUDIyMDEmdGltZXN0YW1wPTE2OTUxMTA1NTk0MDUmdmVyc2lvbj12MQ.g7mZ4c4VZzuwzXBZEDZzoleHdSGwySI5Y8WW6pBfUWcwAAAAAQAAAABlCVWfcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ',
        'av-timezone': 'America/Los_Angeles',
        's_cc': 'true',
        's_nr': '1695111033104-New',
        's_vnum': '2127111033104%26vn%3D1',
        's_dslv': '1695111033104',
        's_sq': '%5B%5BB%5D%5D',
        's_ppv': '40',
        'session-token': '5ll+K6fHu0s44sfMMgUIJ2Nr7Q7MxNl25zVirLg3IGia780gaKCYviO8hbf10GVVSoHoNr9zZt5sbq1Q0GKVdUkZAkVb8sfxdPLPbbmzcwhdoD3vb9MGDeffc/+tiY2wb2u8Zw51GmewbgOAz7WF44vMAJiuoNiDQh/KPj2t5TWVOneI/L039hcAWgTQ+mfn1JvfHUr1PCu/Ax0rY2tPeyeEJt9Pp9qa2OBcH1P6TJ7jsDNK6p0xgwJ2ewhmIxovbLo/J2lGYuEckzi+4bQtVBlcTNspiTijQ3onNCWrBBKD8XpWORJ8XkX1R8RcELAAeS7/4msmTw5TCx9h8HGMz4yartio55Cj6Be0iITaU6dMHGT82oUvDjj2GwAUhhW/',
        'csm-hit': 'tb:s-AYR8CRTC44FR0TXWRWZW|1695116762754&t:1695116763140&adb:adblk_no',
    }
    
    headers = {
        'authority': 'www.amazon.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'session-id=131-0213689-2063762; sp-cdn="L5Z9:PK"; ubid-main=131-5842464-5946415; x-main="2X?zoebw84DaY0Q301zfFDDflVhiGYLdPFuPi4Gst?u5TdejNhgvt5c5se6bf6W@"; at-main=Atza|IwEBIOA4ucmS27lGBX9JqLT8MZMPhIydaKlgT77gvL-5BygrRNCeSeJn7cflJS_AOCCmZsBOoDiupjo7j7QMFJR0fdohAO_D8sM6DzMFp8DXVkBLEMor3DMFJhsytoGLL43ulMpcRip5OKSXVv2Rc8ZFAUiey3vbRZAqi1f9KrDdcBCKRYQ6nyk_95sTA_7U8JWCrThsYvqqqy8BPNRmoQRUzrnFY3finSC-ZS5MucgVUVVFNA; sess-at-main="oWkmFySL3Xn1jZ+/MrhNDzAYeqy35bBAVRKf/NUF2aA="; sst-main=Sst1|PQE48cvsPuFqYcSgTtYkKOWRCWA1-dwmYPOr-sEMxQytNjW_JM9Eo7E9dkK8T9QFBkwNf4MifEhb4vm-j5eXWJzHA9_WJ_GQ-4TS-AngRuhU2AjLOYubeffK8hbpUCH-ab6S8o43mGjesmgi44h2O5vrLWFKbwts23hC7MUyqi7AyGHgRF7gJBmn39-EJwSrK1U3S01dS3fdYHO5_fqJq-D2yBoV6Rc-WWJr4r-fkxHlFsJLSzRhJknSS9fn0S4jg52C6nDBHb-8CQdk3Vbh-ifeVjJrryt7vY8FnFpQnM5gnfI; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; ld=AZUSSOA-sell; s_pers=%20s_fid%3D1D9241E4A786C0DB-342FC1ADB15D3CB4%7C1852886031145%3B%20s_dl%3D1%7C1695035031145%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1695035031146%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271695033231150%2527%255D%255D%7C1852886031150%3B; skin=noskin; av-profile=cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTNJSTdSVEpDUDIyMDEmdGltZXN0YW1wPTE2OTUxMTA1NTk0MDUmdmVyc2lvbj12MQ.g7mZ4c4VZzuwzXBZEDZzoleHdSGwySI5Y8WW6pBfUWcwAAAAAQAAAABlCVWfcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ; av-timezone=America/Los_Angeles; s_cc=true; s_nr=1695111033104-New; s_vnum=2127111033104%26vn%3D1; s_dslv=1695111033104; s_sq=%5B%5BB%5D%5D; s_ppv=40; session-token=5ll+K6fHu0s44sfMMgUIJ2Nr7Q7MxNl25zVirLg3IGia780gaKCYviO8hbf10GVVSoHoNr9zZt5sbq1Q0GKVdUkZAkVb8sfxdPLPbbmzcwhdoD3vb9MGDeffc/+tiY2wb2u8Zw51GmewbgOAz7WF44vMAJiuoNiDQh/KPj2t5TWVOneI/L039hcAWgTQ+mfn1JvfHUr1PCu/Ax0rY2tPeyeEJt9Pp9qa2OBcH1P6TJ7jsDNK6p0xgwJ2ewhmIxovbLo/J2lGYuEckzi+4bQtVBlcTNspiTijQ3onNCWrBBKD8XpWORJ8XkX1R8RcELAAeS7/4msmTw5TCx9h8HGMz4yartio55Cj6Be0iITaU6dMHGT82oUvDjj2GwAUhhW/; csm-hit=tb:s-AYR8CRTC44FR0TXWRWZW|1695116762754&t:1695116763140&adb:adblk_no',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.amazon.com/gp/profile/amzn1.account.AFV2KSFLWI3OUOVJMMA5Y3XOEFKA/ref=cm_cr_dp_d_gw_tr?ie=UTF8',
        'rtt': '0',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '1920',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '1920',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    params = {
        'ownerView': 'false',
        'customerFollowEnabled': 'false',
    }
    
    response = requests.get(
        'https://www.amazon.com/hz/gamification/api/contributor/dashboard/amzn1.account.'+user+'',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response


def reviews(id):    
    cookies = {
        'session-id': '131-0213689-2063762',
        'sp-cdn': '"L5Z9:PK"',
        'ubid-main': '131-5842464-5946415',
        'x-main': '"2X?zoebw84DaY0Q301zfFDDflVhiGYLdPFuPi4Gst?u5TdejNhgvt5c5se6bf6W@"',
        'at-main': 'Atza|IwEBIOA4ucmS27lGBX9JqLT8MZMPhIydaKlgT77gvL-5BygrRNCeSeJn7cflJS_AOCCmZsBOoDiupjo7j7QMFJR0fdohAO_D8sM6DzMFp8DXVkBLEMor3DMFJhsytoGLL43ulMpcRip5OKSXVv2Rc8ZFAUiey3vbRZAqi1f9KrDdcBCKRYQ6nyk_95sTA_7U8JWCrThsYvqqqy8BPNRmoQRUzrnFY3finSC-ZS5MucgVUVVFNA',
        'sess-at-main': '"oWkmFySL3Xn1jZ+/MrhNDzAYeqy35bBAVRKf/NUF2aA="',
        'sst-main': 'Sst1|PQE48cvsPuFqYcSgTtYkKOWRCWA1-dwmYPOr-sEMxQytNjW_JM9Eo7E9dkK8T9QFBkwNf4MifEhb4vm-j5eXWJzHA9_WJ_GQ-4TS-AngRuhU2AjLOYubeffK8hbpUCH-ab6S8o43mGjesmgi44h2O5vrLWFKbwts23hC7MUyqi7AyGHgRF7gJBmn39-EJwSrK1U3S01dS3fdYHO5_fqJq-D2yBoV6Rc-WWJr4r-fkxHlFsJLSzRhJknSS9fn0S4jg52C6nDBHb-8CQdk3Vbh-ifeVjJrryt7vY8FnFpQnM5gnfI',
        'lc-main': 'en_US',
        'session-id-time': '2082787201l',
        'i18n-prefs': 'USD',
        'ld': 'AZUSSOA-sell',
        'av-profile': 'cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTNJSTdSVEpDUDIyMDEmdGltZXN0YW1wPTE2OTUxMTA1NTk0MDUmdmVyc2lvbj12MQ.g7mZ4c4VZzuwzXBZEDZzoleHdSGwySI5Y8WW6pBfUWcwAAAAAQAAAABlCVWfcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ',
        'av-timezone': 'America/Los_Angeles',
        's_nr': '1695111033104-New',
        's_vnum': '2127111033104%26vn%3D1',
        's_dslv': '1695111033104',
        's_pers': '%20s_fid%3D1D9241E4A786C0DB-342FC1ADB15D3CB4%7C1852970258988%3B%20s_dl%3D1%7C1695119258989%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1695119258990%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271695117458991%2527%255D%255D%7C1852970258991%3B',
        'session-token': 'wkt2dvePLBHUE7RnPHjEUyMKLDwI0DvugPr1YZoy5lFSoEHXGB2G6x4ls4ykA6YJjRUobX8WsU0wyQJ+D2Vq8IgR6YP2HAvoefGdsjgXlGWAJu/+N3vH1ufnzM9fyrK95d9FMxWFnxLoBAp4OKRfak7xjIRRcqkXRqHWfjZFkacZH73/uuiDy5oJ36XcUWziTywXftWmjxaQYX7eYd+UxbseedwU1z+CVv2eq5Tx13oXihlw9jMfyaYMclbGg+IhtdlwbUrw2wjpHsdHq5O7zdFwS4Zg6Vo9Br4wh3SLUmR3tW549N20oYxlXZe4QVu7HwOwSgYzJ4p4R/hzWmPapeMZ0rWoZWoSJLDAKc+En1l+VcRADuFPcDgUIaWisifU',
        'skin': 'noskin',
        'csm-hit': 'tb:s-4GG7FDP5NYACA9H4XF35|1695183939727&t:1695183939727&adb:adblk_no',
    }
    
    headers = {
        'authority': 'www.amazon.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'session-id=131-0213689-2063762; sp-cdn="L5Z9:PK"; ubid-main=131-5842464-5946415; x-main="2X?zoebw84DaY0Q301zfFDDflVhiGYLdPFuPi4Gst?u5TdejNhgvt5c5se6bf6W@"; at-main=Atza|IwEBIOA4ucmS27lGBX9JqLT8MZMPhIydaKlgT77gvL-5BygrRNCeSeJn7cflJS_AOCCmZsBOoDiupjo7j7QMFJR0fdohAO_D8sM6DzMFp8DXVkBLEMor3DMFJhsytoGLL43ulMpcRip5OKSXVv2Rc8ZFAUiey3vbRZAqi1f9KrDdcBCKRYQ6nyk_95sTA_7U8JWCrThsYvqqqy8BPNRmoQRUzrnFY3finSC-ZS5MucgVUVVFNA; sess-at-main="oWkmFySL3Xn1jZ+/MrhNDzAYeqy35bBAVRKf/NUF2aA="; sst-main=Sst1|PQE48cvsPuFqYcSgTtYkKOWRCWA1-dwmYPOr-sEMxQytNjW_JM9Eo7E9dkK8T9QFBkwNf4MifEhb4vm-j5eXWJzHA9_WJ_GQ-4TS-AngRuhU2AjLOYubeffK8hbpUCH-ab6S8o43mGjesmgi44h2O5vrLWFKbwts23hC7MUyqi7AyGHgRF7gJBmn39-EJwSrK1U3S01dS3fdYHO5_fqJq-D2yBoV6Rc-WWJr4r-fkxHlFsJLSzRhJknSS9fn0S4jg52C6nDBHb-8CQdk3Vbh-ifeVjJrryt7vY8FnFpQnM5gnfI; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; ld=AZUSSOA-sell; av-profile=cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTNJSTdSVEpDUDIyMDEmdGltZXN0YW1wPTE2OTUxMTA1NTk0MDUmdmVyc2lvbj12MQ.g7mZ4c4VZzuwzXBZEDZzoleHdSGwySI5Y8WW6pBfUWcwAAAAAQAAAABlCVWfcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ; av-timezone=America/Los_Angeles; s_nr=1695111033104-New; s_vnum=2127111033104%26vn%3D1; s_dslv=1695111033104; s_pers=%20s_fid%3D1D9241E4A786C0DB-342FC1ADB15D3CB4%7C1852970258988%3B%20s_dl%3D1%7C1695119258989%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1695119258990%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271695117458991%2527%255D%255D%7C1852970258991%3B; session-token=wkt2dvePLBHUE7RnPHjEUyMKLDwI0DvugPr1YZoy5lFSoEHXGB2G6x4ls4ykA6YJjRUobX8WsU0wyQJ+D2Vq8IgR6YP2HAvoefGdsjgXlGWAJu/+N3vH1ufnzM9fyrK95d9FMxWFnxLoBAp4OKRfak7xjIRRcqkXRqHWfjZFkacZH73/uuiDy5oJ36XcUWziTywXftWmjxaQYX7eYd+UxbseedwU1z+CVv2eq5Tx13oXihlw9jMfyaYMclbGg+IhtdlwbUrw2wjpHsdHq5O7zdFwS4Zg6Vo9Br4wh3SLUmR3tW549N20oYxlXZe4QVu7HwOwSgYzJ4p4R/hzWmPapeMZ0rWoZWoSJLDAKc+En1l+VcRADuFPcDgUIaWisifU; skin=noskin; csm-hit=tb:s-4GG7FDP5NYACA9H4XF35|1695183939727&t:1695183939727&adb:adblk_no',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.amazon.com/gp/profile/amzn1.account.AE7FI5TVDPJ5JSDFEDES4WI7KNBQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8',
        'rtt': '150',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-viewport-width': '1920',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '1920',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    params = {
        'nextPageToken': '',
        'filteredContributionTypes': 'productreview',
        'pageSize': '16',
        'directedId': 'amzn1.account.'+id+'',
        'token': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uSWQiOiIxMzEtMDIxMzY4OS0yMDYzNzYyIiwicmVxdWVzdGVyRGlyZWN0ZWRJZCI6ImFtem4xLmFjY291bnQuQUVST1pYU0hKSlVHTFFYU0hET1NBTlJTREpYQSIsImV4cCI6MTY5NTE4NzUzOCwiZGlyZWN0ZWRJZCI6ImFtem4xLmFjY291bnQuQUU3Rkk1VFZEUEo1SlNERkVERVM0V0k3S05CUSJ9.rdLOl50ry18OxegcNe-BwtubpV5w0JqBQKMqbYnD8V4',
    }
    
    response = requests.get('https://www.amazon.com/profilewidget/timeline/visitor', params=params, cookies=cookies, headers=headers)
    return response