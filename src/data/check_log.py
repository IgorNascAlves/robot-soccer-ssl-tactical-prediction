import gzip
import struct
import os

def check_log_file():
    # Caminho do arquivo que acabamos de baixar
    filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", "2023-07-06_09-10_Immortals-vs-ER-Force.log.gz")
    
    if not os.path.exists(filepath):
        print("Arquivo não encontrado. Baixe o log primeiro.")
        return
        
    print(f"Abrindo arquivo compactado: {os.path.basename(filepath)}...\n")
    
    try:
        with gzip.open(filepath, 'rb') as f:
            # 1. Todo log oficial da RoboCup SSL começa com a assinatura (magic string) de 12 bytes
            magic = f.read(12)
            if magic != b'SSL_LOG_FILE':
                print(f"❌ Formato inválido! O arquivo não é um log SSL. Cabeçalho lido: {magic}")
                return
            
            # 2. Em seguida, vêm 4 bytes indicando a versão do arquivo de log (Inteiro 32-bits)
            version_bytes = f.read(4)
            # Tenta decodificar como Big-Endian
            version = struct.unpack('>i', version_bytes)[0]
            
            print("✅ Sucesso! O arquivo é um Log Oficial Válido da RoboCup SSL.")
            print(f"➡️  Assinatura do Arquivo: {magic.decode('utf-8')}")
            print(f"➡️  Versão do Formato: {version}")
            print("\nO arquivo está pronto para ser parseado pelas definições do Protobuf!")
            
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    check_log_file()
