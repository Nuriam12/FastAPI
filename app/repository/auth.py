from sqlalchemy.orm import Session
from app.DB import models
from fastapi import HTTPException, status
from app.hashing import hash
from app.token import create_access_token

def auth_user(usuario, DB: Session):
    # ✅ OAuth2PasswordRequestForm usa atributos
    username = usuario.username
    password = usuario.password

    # Buscar usuario por username
    user = DB.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el username '{username}', por lo tanto no se realiza el login"
        )

    # Verificar la contraseña
    if not hash.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )

    # Generar el token JWT
    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
