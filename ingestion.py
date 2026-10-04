import requests
import time

def get_btc_transactions(address):
    print(f"Tentative de connexion (BlockCypher) pour l'adresse BTC: {address}...")
    
    # API BlockCypher publique (idéale pour les tests, pas de clé requise)
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}?limit=5"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- SUCCÈS : 5 Dernières transactions ---")
            
            # Les transactions sont dans 'txrefs' ou 'unconfirmed_txrefs'
            txs = data.get('txrefs', [])[:5]
            if not txs:
                print("Aucune transaction trouvée pour cette adresse.")
                return

            for tx in txs:
                valeur_btc = tx.get('value', 0) / 10**8
                print(f"Hash TX: {tx.get('tx_hash', 'N/A')[:15]}... | Date: {tx.get('confirmed', 'Non confirmée')} | Valeur: {valeur_btc:.4f} BTC")
        else:
            print(f"\nÉchec de l'API: HTTP {response.status_code}")
            print(f"Détail: {response.text}")
            
    except Exception as e:
        print(f"Erreur de connexion : {e}")

# Adresse BTC test (Binance)
test_address = "34xp4vRoCGJym3xR7yCVPFHoJQvxvrCEcg"
get_btc_transactions(test_address)

