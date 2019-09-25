import requests

r = requests.get('https://www.amazon.cn/dp/B07FK7BPJP?smid=A3TEGLC21NOO5Y&ref_=Oct_CBBBCard_dsk_asin2&pf_rd_r=08JN2ZM838DKA0SKZFQ1&pf_rd_p=3f974805-ea47-43ca-9f36-30f77be0fad9&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-3')
print(r.status_code)
print(r.request.headers)
#更改头部信息
kv = {'user-agent':'Mozilla/5.0'}
url = 'https://www.amazon.cn/dp/B07FK7BPJP?smid=A3TEGLC21NOO5Y&ref_=Oct_CBBBCard_dsk_asin2&pf_rd_r=08JN2ZM838DKA0SKZFQ1&pf_rd_p=3f974805-ea47-43ca-9f36-30f77be0fad9&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-3'
r = requests.get(url,headers = kv)
print(r.status_code)