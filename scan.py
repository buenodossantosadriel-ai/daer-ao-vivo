import requests
cidades = [
"porto_alegre","canoas","pelotas","santa_maria","caxias_do_sul","ijui","passo_fundo",
"uruguaiana","bento_goncalves","erechim","santa_cruz_do_sul","lajeado","santana_do_livramento",
"bagé","bage","rio_grande","santo_angelo","vacaria","carazinho","gramado","canela",
"torres","osorio","tramandai","capao_da_canoa","farroupilha","montenegro","portao",
"lajeado","santa_rosa","frederico_westphalen","sao_borja","sao_gabriel","alegrete",
"cachoeira_do_sul","cruz_alta","panambi","sao_leopoldo","novo_hamburgo","gravatai",
"viamao","guaiba","eldorado_do_sul","charqueadas","butia","camaqua","sao_lourenco_do_sul"
]
for c in cidades:
    url = f"https://daer.kopp.com.br/sistrak-base-010/rs/importacao/camera-importador-operacao-registro/codigo-camera/ptz_{c}"
    try:
        r = requests.get(url, timeout=5, headers={"Referer":"https://www.daer.rs.gov.br/cameras-de-monitoramento"})
        if r.status_code==200 and len(r.content)>5000:
            print(f"✅ ENCONTREI: ptz_{c} - {len(r.content)} bytes")
        else:
            print(f"❌ {c} - {r.status_code}")
    except Exception as e:
        print(f"erro {c}")
