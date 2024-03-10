from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configuración del servidor FTP
FTP_HOST = '0.0.0.0'  # Todas las interfaces
FTP_PORT = 2121  # Puerto FTP personalizado
FTP_USER = 'admin'
FTP_PASSWORD = 'admin'
FTP_DIRECTORY = '/home'  # Directorio home del usuario "admin"

# Crear un autorizador dummy para el servidor FTP
authorizer = DummyAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

# Crear un manejador FTP
handler = FTPHandler
handler.authorizer = authorizer

# Configurar el directorio base
handler.user_virtual_paths = {FTP_USER: FTP_DIRECTORY}

# Configurar el servidor FTP
server = FTPServer((FTP_HOST, FTP_PORT), handler)

# Iniciar el servidor FTP
server.serve_forever()
