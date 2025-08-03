import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi

from src import agenda_router
from src.redis_funcs import startup_event, shutdown_event

app = FastAPI(title="Agenda", version="1.0.0",
              description="Esta API tem como objetivo simular uma agenda.")

app.include_router(agenda_router.router)

@app.on_event("startup")
async def startup():
    await startup_event()


@app.on_event("shutdown")
async def shutdown():
    await shutdown_event()


@app.get("/health", status_code=200)
async def service_health():
    return {"ok"}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>Bem-vindo à API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: #fff;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #0056b3;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                ul li {
                    margin-bottom: 10px;
                }
                a {
                    color: #0056b3;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                footer {
                    margin-top: 20px;
                    text-align: center;
                    font-size: 0.9em;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bem-vindo a API Agenda</h1>
                </ul>
                <p>Essa API foi desenvolvida pelo Aluno Lorenzo Moreira Donatti para a disciplina ECD14</p>
                </ul>
                <p>Interface FrontEnd não desenvolvida. Para testar vá para o /docs ou execute o script test_api.py</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)