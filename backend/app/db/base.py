from app.db.session import Base

# Re-export Base for all models
# This ensures consistent metadata across the application
__all__ = ["Base"]
