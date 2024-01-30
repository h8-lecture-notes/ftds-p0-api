# fastapi -> membuat api
# uvicorn -> menjalankan api/server
from fastapi import FastAPI, HTTPException, Request, Response
import pandas as pd

# membuat object FastAPI
app = FastAPI()

# dataframe
df = pd.DataFrame({
    "names": ['yuda', 'hyuga', 'tsubasa'],
    "locations": ['Jakarta', 'Toho', 'Nankatsu']
})

# # mendaftarkan endpoint / url
# @app.get('/')  # halaman utama
# def getHome(request: Request):
#     # melihat isi headers dari request
#     headers = request.headers

#     # membuat response
#     response = Response("ini halaman utama coy")

#     # return json data
#     return {
#         "req-headers": headers,
#         "response-headers": response.headers,
#         "response-body":response.body
#     }

# mendaftarkan endpoint / url
@app.get('/')  # halaman utama
def getHome(request: Request):
    return {
        "message": "ini halaman utama"
    }

@app.get('/names/{name}')
def findName(name):
    # filter df
    result = df[df['names'] == name]

    # jika ada data -> tampilkan
    # jika tidak ada -> error 404
    if len(result) == 0:
        # kasih exception
        raise HTTPException(status_code=404, detail="Data Tidak Ditemukan")
    else:
        # return hasil filter
        return result.to_dict(orient='records')

# endpoint untuk melihat seluruh data di df
@app.get('/see-all')
def getSeeAll():
    # orient = dict (default)
    # awal: {
    #   column : {index:value}, ...,
    #   column : {index:value}
    # }

    # orient = records
    # expectation: [
    #   {column: value},
    #   {column: value},
    # ]

    # return data from dataframe
    return df.to_dict(orient='records')
