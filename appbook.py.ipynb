{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bc8c9fbb-a275-467e-a7a1-2e417954ff1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HP\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\computation\\expressions.py:22: UserWarning: Pandas requires version '2.10.2' or newer of 'numexpr' (version '2.8.7' currently installed).\n",
      "  from pandas.core.computation.check import NUMEXPR_INSTALLED\n",
      "C:\\Users\\HP\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\arrays\\masked.py:56: UserWarning: Pandas requires version '1.4.2' or newer of 'bottleneck' (version '1.3.7' currently installed).\n",
      "  from pandas.core import (\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "\n",
    "popular_df = pickle.load(\n",
    "    open('popular.pkl','rb')\n",
    ")\n",
    "\n",
    "pt = pickle.load(\n",
    "    open('pivot.pkl','rb')\n",
    ")\n",
    "\n",
    "similarity_scores = pickle.load(\n",
    "    open('similarity.pkl','rb')\n",
    ")\n",
    "\n",
    "books = pickle.load(\n",
    "    open('books.pkl','rb')\n",
    ")\n",
    "\n",
    "content_similarity = pickle.load(\n",
    "    open('content_similarity.pkl','rb')\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7d718404-29da-403f-9b52-121a2ddab94b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hybrid_recommend(book_name):\n",
    "\n",
    "    collab = collaborative_recommend(book_name)\n",
    "\n",
    "    try:\n",
    "        content = content_recommend(book_name)\n",
    "        content = list(content)\n",
    "\n",
    "    except:\n",
    "        content = []\n",
    "\n",
    "    final = list(\n",
    "        dict.fromkeys(\n",
    "            collab + content\n",
    "        )\n",
    "    )\n",
    "\n",
    "    return final[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2241b9c6-8ac7-4985-9e11-cb69f7edd235",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "st.set_page_config(\n",
    "    page_title=\"Book Recommendation System\",\n",
    "    page_icon=\"📚\",\n",
    "    layout=\"wide\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a4a91fbb-affe-41b9-9b44-76aae0ce49cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-06-23 11:50:46.657 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\anaconda3\\anaconda1\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown(\"\"\"\n",
    "<style>\n",
    "\n",
    ".main {\n",
    "    background-color:#f5f7fa;\n",
    "}\n",
    "\n",
    ".title {\n",
    "    text-align:center;\n",
    "    font-size:50px;\n",
    "    font-weight:bold;\n",
    "    color:#1f4e79;\n",
    "}\n",
    "\n",
    ".subtitle {\n",
    "    text-align:center;\n",
    "    font-size:20px;\n",
    "    color:gray;\n",
    "}\n",
    "\n",
    ".recommendation-card {\n",
    "    background-color:white;\n",
    "    padding:15px;\n",
    "    border-radius:10px;\n",
    "    box-shadow:0px 2px 8px rgba(0,0,0,0.2);\n",
    "}\n",
    "\n",
    "</style>\n",
    "\"\"\", unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5428466f-720e-4065-a395-bcc336411fd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown(\n",
    "    \"<p class='title'>📚 Book Recommendation System</p>\",\n",
    "    unsafe_allow_html=True\n",
    ")\n",
    "\n",
    "st.markdown(\n",
    "    \"<p class='subtitle'>AI Powered Book Recommendation Engine</p>\",\n",
    "    unsafe_allow_html=True\n",
    ")\n",
    "\n",
    "st.write(\"---\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fa1f2e75-ddf1-4483-8feb-2e7af7937227",
   "metadata": {},
   "outputs": [],
   "source": [
    "popular_df = pickle.load(\n",
    "    open('popular.pkl','rb')\n",
    ")\n",
    "\n",
    "pt = pickle.load(\n",
    "    open('pivot.pkl','rb')\n",
    ")\n",
    "\n",
    "similarity_scores = pickle.load(\n",
    "    open('similarity.pkl','rb')\n",
    ")\n",
    "\n",
    "books = pickle.load(\n",
    "    open('books.pkl','rb')\n",
    ")\n",
    "\n",
    "content_similarity = pickle.load(\n",
    "    open('content_similarity.pkl','rb')\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "25a7a836-a10b-4751-b4a8-b61471647a2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-06-23 11:51:34.277 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "st.sidebar.title(\"Navigation\")\n",
    "\n",
    "page = st.sidebar.radio(\n",
    "    \"Choose Page\",\n",
    "    [\n",
    "        \"Home\",\n",
    "        \"Recommend Books\"\n",
    "    ]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a875ff6b-675d-4560-921b-7dd1098a0378",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"None of [Index(['Book-Title', 'Book-Author'], dtype='str')] are in the [columns]\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[16], line 6\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m page \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHome\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m      3\u001b[0m     st\u001b[38;5;241m.\u001b[39msubheader(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPopular Books\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      5\u001b[0m     st\u001b[38;5;241m.\u001b[39mdataframe(\n\u001b[1;32m----> 6\u001b[0m         popular_df[\n\u001b[0;32m      7\u001b[0m             [\n\u001b[0;32m      8\u001b[0m                 \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBook-Title\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m      9\u001b[0m                 \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBook-Author\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m     10\u001b[0m             ]\n\u001b[0;32m     11\u001b[0m         ]\u001b[38;5;241m.\u001b[39mhead(\u001b[38;5;241m10\u001b[39m)\n\u001b[0;32m     12\u001b[0m     )\n",
      "File \u001b[1;32m~\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\frame.py:4384\u001b[0m, in \u001b[0;36mDataFrame.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   4382\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m is_iterator(key):\n\u001b[0;32m   4383\u001b[0m         key \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlist\u001b[39m(key)\n\u001b[1;32m-> 4384\u001b[0m     indexer \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcolumns\u001b[38;5;241m.\u001b[39m_get_indexer_strict(key, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcolumns\u001b[39m\u001b[38;5;124m\"\u001b[39m)[\u001b[38;5;241m1\u001b[39m]\n\u001b[0;32m   4386\u001b[0m \u001b[38;5;66;03m# take() does not accept boolean indexers\u001b[39;00m\n\u001b[0;32m   4387\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(indexer, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdtype\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m) \u001b[38;5;241m==\u001b[39m \u001b[38;5;28mbool\u001b[39m:\n",
      "File \u001b[1;32m~\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:6302\u001b[0m, in \u001b[0;36mIndex._get_indexer_strict\u001b[1;34m(self, key, axis_name)\u001b[0m\n\u001b[0;32m   6299\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m   6300\u001b[0m     keyarr, indexer, new_indexer \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_reindex_non_unique(keyarr)\n\u001b[1;32m-> 6302\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_raise_if_missing(keyarr, indexer, axis_name)\n\u001b[0;32m   6304\u001b[0m keyarr \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtake(indexer)\n\u001b[0;32m   6305\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, Index):\n\u001b[0;32m   6306\u001b[0m     \u001b[38;5;66;03m# GH 42790 - Preserve name from an Index\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\anaconda1\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:6352\u001b[0m, in \u001b[0;36mIndex._raise_if_missing\u001b[1;34m(self, key, indexer, axis_name)\u001b[0m\n\u001b[0;32m   6350\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m nmissing:\n\u001b[0;32m   6351\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m nmissing \u001b[38;5;241m==\u001b[39m \u001b[38;5;28mlen\u001b[39m(indexer):\n\u001b[1;32m-> 6352\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNone of [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mkey\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m] are in the [\u001b[39m\u001b[38;5;132;01m{\u001b[39;00maxis_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m]\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m   6354\u001b[0m     not_found \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlist\u001b[39m(ensure_index(key)[missing_mask\u001b[38;5;241m.\u001b[39mnonzero()[\u001b[38;5;241m0\u001b[39m]]\u001b[38;5;241m.\u001b[39munique())\n\u001b[0;32m   6355\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mnot_found\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m not in index\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mKeyError\u001b[0m: \"None of [Index(['Book-Title', 'Book-Author'], dtype='str')] are in the [columns]\""
     ]
    }
   ],
   "source": [
    "if page == \"Home\":\n",
    "\n",
    "    st.subheader(\"Popular Books\")\n",
    "\n",
    "    st.dataframe(\n",
    "        popular_df[\n",
    "            [\n",
    "                'Book-Title',\n",
    "                'Book-Author'\n",
    "            ]\n",
    "        ].head(10)\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1478a5f7-4ab8-44a4-9522-db64e69aa3a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (base)",
   "language": "python",
   "name": "base"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
