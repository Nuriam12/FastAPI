from sqlalchemy.orm import Session
from app.DB import models
from fastapi import HTTPException,status
from app.hashing import hash
from app.token import create_access_token

def auth_user(usuario,DB:Session):
    usuario = usuario.dict()
    user = DB.query(models.User).filter(models.User.username==usuario["username"]).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"no existe el usuario con el username {usuario["username"]} por lo tanto no se realiza el login"
        )
    
    print("Este es la contraseña -> ",hash.verify_password(usuario["password"],user.password))

    if not hash.verify_password(usuario["password"],user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"CONTRASEÑA INCORRECTA"
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token":access_token, "token_type":"bearer"}
