import urllib.request
import os

def download_sample_log():
    # Link direto para um jogo oficial da Divisão A (RoboCup 2023: Immortals vs ER-Force)
    # Hospedado no Seafile público da TIGERs Mannheim
    download_url = "https://seafile.tigers-mannheim.de/d/e85851d9bc9944bf95bb/files/?p=/gamelogs/2023/div-a/2023-07-06_09-10_Immortals-vs-ER-Force.log.gz&dl=1"
    target_file = "2023-07-06_09-10_Immortals-vs-ER-Force.log.gz"
    
    print(f"Buscando log oficial da Robot Soccer SSL...")
    
    try:
        # Cria a pasta data/raw se não existir
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, target_file)
        
        print(f"Baixando arquivo: {target_file}")
        print("Isso pode demorar alguns minutos, os arquivos têm ~50MB compactados...")
        
        # Faz o download
        req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
            out_file.write(response.read())
            
        print(f"Download concluído com sucesso! Salvo em: {output_path}")
        
    except Exception as e:
        print(f"Erro ao baixar o log: {e}")

if __name__ == "__main__":
    download_sample_log()
