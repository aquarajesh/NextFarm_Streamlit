import streamlit as st
import json
from google.cloud import firestore
from google.oauth2 import service_account
import pandas as pd
import farmdata as fd

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="nextaqua-22991")

checktray_ref = db.collection("checktraydata")
checktray_docs = (
    db.collection("checktraydata").where("isRealSite", "==", True)
    .stream()
)
# And then render each post, using some light Markdown
for doc in checktray_docs:
	fd.displayDocument(doc)


# doc_ref = db.collection("checktraydata").document("AGV2402246188")
# doc = doc_ref.get()
# fd.displayDocument(doc)


     

# Add final separator to end of grid


