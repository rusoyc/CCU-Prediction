{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        purchases = request.form.get(\"purchases\")\n",
    "        suppcard = request.form.get(\"suppcard\")\n",
    "        print(purchases,suppcard)\n",
    "        \n",
    "        purchases = float(purchases)\n",
    "        suppcard = float(suppcard)\n",
    "        \n",
    "        model1 = joblib.load(\"CART\")\n",
    "        pred1 = model1.predict([[purchases,suppcard]])\n",
    "\n",
    "        model2 = joblib.load(\"RF\")\n",
    "        pred2 = model2.predict([[purchases,suppcard]])\n",
    "        \n",
    "        model3 = joblib.load(\"GB\")\n",
    "        pred3 = model3.predict([[purchases,suppcard]])\n",
    "        return(render_template(\"index.html\",result1=pred1,result2=pred2,result3=pred3))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result1=\"\",result2=\"\",result3=\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: Do not use the development server in a production environment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [26/Mar/2022 16:18:12] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34 0\n",
      "34 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [26/Mar/2022 16:18:20] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [26/Mar/2022 16:18:20] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [26/Mar/2022 16:18:26] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [26/Mar/2022 16:22:08] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [26/Mar/2022 16:22:10] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [26/Mar/2022 16:22:16] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [26/Mar/2022 16:22:21] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20 1\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
