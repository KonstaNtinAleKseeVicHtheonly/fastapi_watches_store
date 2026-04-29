# backend/core/middleware.py
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.core.config import project_settings

def setup_cors(app: FastAPI):
    """Настройка CORS для приложения"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=project_settings.CORS_ORIGINS,  # из config
        allow_credentials=True, #отправка куков заголовков при запросах  с фронта на наш  домен
        allow_methods=project_settings.ALLOWED_METHODS,
        allow_headers=project_settings.ALLOWED_HEADERS,
    )