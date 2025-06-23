# 🏋️‍♀️ Workout Tracker with Nutritionix API

Este é um pequeno projeto em Python que regista automaticamente os teus treinos, calcula calorias queimadas e envia os dados para um Google Sheet, usando as APIs da [Nutritionix](https://www.nutritionix.com/business/api) e Sheety.

## ✨ Funcionalidades

- Usa linguagem natural (ex: `"corrida 30 minutos"` ou `"fiz 10 minutos de futsal"`)
- Calcula automaticamente calorias, duração e tipo de exercício
- Regista os dados num Google Sheet com:
  - 📅 Data
  - 🕒 Hora
  - 🏃 Tipo de exercício
  - ⏱️ Duração (minutos)
  - 🔥 Calorias gastas

---

## 📦 Tecnologias

- [Nutritionix API](https://developer.nutritionix.com/) — para interpretar o exercício
- [Sheety](https://sheety.co/) — para guardar os dados em Google Sheets
- `dotenv` — para proteger as chaves de API
- `requests` — para chamadas HTTP

---

## 🔐 Variáveis de Ambiente

Cria um ficheiro `.env` no diretório principal com o seguinte conteúdo:

```env
app_id=O_TEU_APP_ID_DA_NUTRITIONIX
app_key=A_TUA_API_KEY_DA_NUTRITIONIX
sheety_endpoint=https://api.sheety.co/TEU_ENDPOINT/folder/folha1
sheety_username=O_TEU_UTILIZADOR (opcional, se usares auth básica)
sheety_password=A_TUA_PASSWORD (opcional)
```
---
## 📝 Exemplo de resposta
```
{
  "exercises": [
    {
      "name": "soccer",
      "duration": 30,
      "calories": 200
    }
  ]
}
```
