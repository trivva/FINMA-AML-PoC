import requests

def get_btc_transactions(address):
    print(f"Recherche on-chain pour l'adresse: {address}...\n")
    # API publique Blockchain.com (aucune clé requise)
    url = f"https://blockchain.info/rawaddr/{address}?limit=5"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("--- SUCCÈS : 5 DERNIÈRES TRANSACTIONS ---")
            for tx in data.get('txs', []):
                print(f"Hash TX: {tx.get('hash')[:20]}... | Taille: {tx.get('size')} bytes")
        else:
            print(f"Échec de connexion API (Code HTTP {response.status_code})")
    except Exception as e:
        print(f"Erreur locale: {e}")

# Test avec l'adresse Binance
target_address = "34xp4vRoCGJym3xR7yCVPFHoJQvxvrCEcg"
get_btc_transactions(target_address)