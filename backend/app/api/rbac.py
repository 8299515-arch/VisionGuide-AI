from fastapi import Depends, HTTPException, status

from app.api.deps import get_current_user
from app.models.user import User


def require_role(allowed_roles: list[str]):
    def role_checker(current_user: User = Depends(get_current_user)):
        # NOTE: in future we will join Role table; for now use simple string role_id
        if not current_user.role_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Role not assigned",
            )

        if current_user.role_id not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )

        return current_user

    return role_checker
