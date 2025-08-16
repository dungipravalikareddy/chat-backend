from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import chat as chat_ep
from app.core.config import get_settings
from app.core.logging_config import configure_logging
from app.middlewares.timing import TimingMiddleware
from app.api.v1.endpoints import health as health_ep
from app.api.v1.endpoints import auth as auth_ep
from app.api.v1.endpoints import analytics as analytics_ep


def create_app() -> FastAPI:
    configure_logging()
    settings = get_settings()

    app = FastAPI(
        title="Chat Backend",
        version="1.0.0",
        description="LLM-powered chatbot backend"
    )

    app.add_middleware(TimingMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # API version prefix
    api_prefix = "/api/v1"

    # Routers
    app.include_router(health_ep.router, prefix=f"{api_prefix}/health", tags=["health"])
    app.include_router(chat_ep.router, prefix=f"{api_prefix}/chat", tags=["chat"])
    app.include_router(analytics_ep.router, prefix="/api/v1/analytics", tags=["analytics"])
    app.include_router(auth_ep.router, prefix="/api/v1/auth", tags=["Auth"])

    return app

app = create_app()
