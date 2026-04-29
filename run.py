import uvicorn
from backend.core.config import project_settings

if __name__ == "__main__":
    uvicorn.run(
        'backend.main:app',
        host='0.0.0.0',
        port=project_settings.APP_PORT,
        reload=project_settings.DEBUG,
        log_level='info',
    )