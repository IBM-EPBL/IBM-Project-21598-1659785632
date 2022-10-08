{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "0109af19",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import scipy\n",
    "from scipy import stats\n",
    "from sklearn.preprocessing import OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9dcca9f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_csv(\"C:\\\\Users\\\\Devi\\\\Downloads\\\\abalone.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4e68877e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sex</th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>0.455</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.5140</td>\n",
       "      <td>0.2245</td>\n",
       "      <td>0.1010</td>\n",
       "      <td>0.1500</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>0.350</td>\n",
       "      <td>0.265</td>\n",
       "      <td>0.090</td>\n",
       "      <td>0.2255</td>\n",
       "      <td>0.0995</td>\n",
       "      <td>0.0485</td>\n",
       "      <td>0.0700</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>0.530</td>\n",
       "      <td>0.420</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.6770</td>\n",
       "      <td>0.2565</td>\n",
       "      <td>0.1415</td>\n",
       "      <td>0.2100</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.5160</td>\n",
       "      <td>0.2155</td>\n",
       "      <td>0.1140</td>\n",
       "      <td>0.1550</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>I</td>\n",
       "      <td>0.330</td>\n",
       "      <td>0.255</td>\n",
       "      <td>0.080</td>\n",
       "      <td>0.2050</td>\n",
       "      <td>0.0895</td>\n",
       "      <td>0.0395</td>\n",
       "      <td>0.0550</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4172</th>\n",
       "      <td>F</td>\n",
       "      <td>0.565</td>\n",
       "      <td>0.450</td>\n",
       "      <td>0.165</td>\n",
       "      <td>0.8870</td>\n",
       "      <td>0.3700</td>\n",
       "      <td>0.2390</td>\n",
       "      <td>0.2490</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4173</th>\n",
       "      <td>M</td>\n",
       "      <td>0.590</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.9660</td>\n",
       "      <td>0.4390</td>\n",
       "      <td>0.2145</td>\n",
       "      <td>0.2605</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4174</th>\n",
       "      <td>M</td>\n",
       "      <td>0.600</td>\n",
       "      <td>0.475</td>\n",
       "      <td>0.205</td>\n",
       "      <td>1.1760</td>\n",
       "      <td>0.5255</td>\n",
       "      <td>0.2875</td>\n",
       "      <td>0.3080</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4175</th>\n",
       "      <td>F</td>\n",
       "      <td>0.625</td>\n",
       "      <td>0.485</td>\n",
       "      <td>0.150</td>\n",
       "      <td>1.0945</td>\n",
       "      <td>0.5310</td>\n",
       "      <td>0.2610</td>\n",
       "      <td>0.2960</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4176</th>\n",
       "      <td>M</td>\n",
       "      <td>0.710</td>\n",
       "      <td>0.555</td>\n",
       "      <td>0.195</td>\n",
       "      <td>1.9485</td>\n",
       "      <td>0.9455</td>\n",
       "      <td>0.3765</td>\n",
       "      <td>0.4950</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4177 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Sex  Length  Diameter  Height  Whole weight  Shucked weight  \\\n",
       "0      M   0.455     0.365   0.095        0.5140          0.2245   \n",
       "1      M   0.350     0.265   0.090        0.2255          0.0995   \n",
       "2      F   0.530     0.420   0.135        0.6770          0.2565   \n",
       "3      M   0.440     0.365   0.125        0.5160          0.2155   \n",
       "4      I   0.330     0.255   0.080        0.2050          0.0895   \n",
       "...   ..     ...       ...     ...           ...             ...   \n",
       "4172   F   0.565     0.450   0.165        0.8870          0.3700   \n",
       "4173   M   0.590     0.440   0.135        0.9660          0.4390   \n",
       "4174   M   0.600     0.475   0.205        1.1760          0.5255   \n",
       "4175   F   0.625     0.485   0.150        1.0945          0.5310   \n",
       "4176   M   0.710     0.555   0.195        1.9485          0.9455   \n",
       "\n",
       "      Viscera weight  Shell weight  Rings  \n",
       "0             0.1010        0.1500     15  \n",
       "1             0.0485        0.0700      7  \n",
       "2             0.1415        0.2100      9  \n",
       "3             0.1140        0.1550     10  \n",
       "4             0.0395        0.0550      7  \n",
       "...              ...           ...    ...  \n",
       "4172          0.2390        0.2490     11  \n",
       "4173          0.2145        0.2605     10  \n",
       "4174          0.2875        0.3080      9  \n",
       "4175          0.2610        0.2960     10  \n",
       "4176          0.3765        0.4950     12  \n",
       "\n",
       "[4177 rows x 9 columns]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5603331",
   "metadata": {},
   "source": [
    "# Univariate Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "57c40e94",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_1=dataset.loc[dataset['Rings']==7]\n",
    "df_2=dataset.loc[dataset['Rings']==9]\n",
    "df_3=dataset.loc[dataset['Rings']==10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4d877893",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(df_1['Sex'],np.zeros_like(df_1['Sex']))\n",
    "plt.plot(df_2['Sex'],np.zeros_like(df_2['Sex']))\n",
    "plt.plot(df_3['Sex'],np.zeros_like(df_3['Sex']))\n",
    "plt.xlabel('Sex')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f52702b5",
   "metadata": {},
   "source": [
    "# Bi-Variate Analysis\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e8290d26",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\anaconda3\\lib\\site-packages\\seaborn\\axisgrid.py:337: UserWarning: The `size` parameter has been renamed to `height`; please update your code.\n",
      "  warnings.warn(msg, UserWarning)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 408.75x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.FacetGrid(dataset,hue=\"Rings\",size=5).map(plt.scatter,\"Length\",\"Height\").add_legend();"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "074af1c0",
   "metadata": {},
   "source": [
    "# Multi-Variate Analysis\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "86336be3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\anaconda3\\lib\\site-packages\\seaborn\\axisgrid.py:2076: UserWarning: The `size` parameter has been renamed to `height`; please update your code.\n",
      "  warnings.warn(msg, UserWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x1e71ab33d60>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 2568.75x2520 with 56 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(dataset,hue=\"Rings\",size=5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73f7748f",
   "metadata": {},
   "source": [
    "# Descriptive statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b7dca7cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sex               MMFMIIFFMFFMMFFMIFMMMIFFFFFMMMMFMFFMFFFMFFIIII...\n",
       "Length                                                     2188.715\n",
       "Diameter                                                    1703.72\n",
       "Height                                                       582.76\n",
       "Whole weight                                               3461.656\n",
       "Shucked weight                                             1501.078\n",
       "Viscera weight                                             754.3395\n",
       "Shell weight                                               997.5965\n",
       "Rings                                                         41493\n",
       "dtype: object"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b447d5a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\AppData\\Local\\Temp\\ipykernel_6272\\3445892410.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.\n",
      "  dataset.sum(axis=1)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0       16.9045\n",
       "1        8.1485\n",
       "2       11.3700\n",
       "3       11.9305\n",
       "4        8.0540\n",
       "         ...   \n",
       "4172    13.9250\n",
       "4173    13.0450\n",
       "4174    12.5770\n",
       "4175    13.4425\n",
       "4176    17.2255\n",
       "Length: 4177, dtype: float64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.sum(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "312d56f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\AppData\\Local\\Temp\\ipykernel_6272\\4167803218.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.\n",
      "  dataset.median()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Length            0.5450\n",
       "Diameter          0.4250\n",
       "Height            0.1400\n",
       "Whole weight      0.7995\n",
       "Shucked weight    0.3360\n",
       "Viscera weight    0.1710\n",
       "Shell weight      0.2340\n",
       "Rings             9.0000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9a53fe5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\AppData\\Local\\Temp\\ipykernel_6272\\1799472221.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.\n",
      "  dataset.mean()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Length            0.523992\n",
       "Diameter          0.407881\n",
       "Height            0.139516\n",
       "Whole weight      0.828742\n",
       "Shucked weight    0.359367\n",
       "Viscera weight    0.180594\n",
       "Shell weight      0.238831\n",
       "Rings             9.933684\n",
       "dtype: float64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "79f8bcfe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sex                    M\n",
       "Length             0.815\n",
       "Diameter            0.65\n",
       "Height              1.13\n",
       "Whole weight      2.8255\n",
       "Shucked weight     1.488\n",
       "Viscera weight      0.76\n",
       "Shell weight       1.005\n",
       "Rings                 29\n",
       "dtype: object"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "36825c31",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\AppData\\Local\\Temp\\ipykernel_6272\\178401259.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.\n",
      "  dataset.std()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Length            0.120093\n",
       "Diameter          0.099240\n",
       "Height            0.041827\n",
       "Whole weight      0.490389\n",
       "Shucked weight    0.221963\n",
       "Viscera weight    0.109614\n",
       "Shell weight      0.139203\n",
       "Rings             3.224169\n",
       "dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3980db93",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Devi\\AppData\\Local\\Temp\\ipykernel_6272\\2458428038.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.\n",
      "  dataset.var()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Length             0.014422\n",
       "Diameter           0.009849\n",
       "Height             0.001750\n",
       "Whole weight       0.240481\n",
       "Shucked weight     0.049268\n",
       "Viscera weight     0.012015\n",
       "Shell weight       0.019377\n",
       "Rings             10.395266\n",
       "dtype: float64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.var()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c269a8ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9     689\n",
       "10    634\n",
       "8     568\n",
       "11    487\n",
       "7     391\n",
       "12    267\n",
       "6     259\n",
       "13    203\n",
       "14    126\n",
       "5     115\n",
       "15    103\n",
       "16     67\n",
       "17     58\n",
       "4      57\n",
       "18     42\n",
       "19     32\n",
       "20     26\n",
       "3      15\n",
       "21     14\n",
       "23      9\n",
       "22      6\n",
       "27      2\n",
       "24      2\n",
       "1       1\n",
       "26      1\n",
       "29      1\n",
       "2       1\n",
       "25      1\n",
       "Name: Rings, dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Rings=dataset.Rings\n",
    "Rings.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "dba30ab0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "      <td>4177.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.523992</td>\n",
       "      <td>0.407881</td>\n",
       "      <td>0.139516</td>\n",
       "      <td>0.828742</td>\n",
       "      <td>0.359367</td>\n",
       "      <td>0.180594</td>\n",
       "      <td>0.238831</td>\n",
       "      <td>9.933684</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.120093</td>\n",
       "      <td>0.099240</td>\n",
       "      <td>0.041827</td>\n",
       "      <td>0.490389</td>\n",
       "      <td>0.221963</td>\n",
       "      <td>0.109614</td>\n",
       "      <td>0.139203</td>\n",
       "      <td>3.224169</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.075000</td>\n",
       "      <td>0.055000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.002000</td>\n",
       "      <td>0.001000</td>\n",
       "      <td>0.000500</td>\n",
       "      <td>0.001500</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.450000</td>\n",
       "      <td>0.350000</td>\n",
       "      <td>0.115000</td>\n",
       "      <td>0.441500</td>\n",
       "      <td>0.186000</td>\n",
       "      <td>0.093500</td>\n",
       "      <td>0.130000</td>\n",
       "      <td>8.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.545000</td>\n",
       "      <td>0.425000</td>\n",
       "      <td>0.140000</td>\n",
       "      <td>0.799500</td>\n",
       "      <td>0.336000</td>\n",
       "      <td>0.171000</td>\n",
       "      <td>0.234000</td>\n",
       "      <td>9.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.615000</td>\n",
       "      <td>0.480000</td>\n",
       "      <td>0.165000</td>\n",
       "      <td>1.153000</td>\n",
       "      <td>0.502000</td>\n",
       "      <td>0.253000</td>\n",
       "      <td>0.329000</td>\n",
       "      <td>11.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>0.815000</td>\n",
       "      <td>0.650000</td>\n",
       "      <td>1.130000</td>\n",
       "      <td>2.825500</td>\n",
       "      <td>1.488000</td>\n",
       "      <td>0.760000</td>\n",
       "      <td>1.005000</td>\n",
       "      <td>29.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Length     Diameter       Height  Whole weight  Shucked weight  \\\n",
       "count  4177.000000  4177.000000  4177.000000   4177.000000     4177.000000   \n",
       "mean      0.523992     0.407881     0.139516      0.828742        0.359367   \n",
       "std       0.120093     0.099240     0.041827      0.490389        0.221963   \n",
       "min       0.075000     0.055000     0.000000      0.002000        0.001000   \n",
       "25%       0.450000     0.350000     0.115000      0.441500        0.186000   \n",
       "50%       0.545000     0.425000     0.140000      0.799500        0.336000   \n",
       "75%       0.615000     0.480000     0.165000      1.153000        0.502000   \n",
       "max       0.815000     0.650000     1.130000      2.825500        1.488000   \n",
       "\n",
       "       Viscera weight  Shell weight        Rings  \n",
       "count     4177.000000   4177.000000  4177.000000  \n",
       "mean         0.180594      0.238831     9.933684  \n",
       "std          0.109614      0.139203     3.224169  \n",
       "min          0.000500      0.001500     1.000000  \n",
       "25%          0.093500      0.130000     8.000000  \n",
       "50%          0.171000      0.234000     9.000000  \n",
       "75%          0.253000      0.329000    11.000000  \n",
       "max          0.760000      1.005000    29.000000  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32197b39",
   "metadata": {},
   "source": [
    "# Missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "07c331f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4177, 9)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2ef3b51d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sex</th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4172</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4173</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4174</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4175</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4176</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4177 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        Sex  Length  Diameter  Height  Whole weight  Shucked weight  \\\n",
       "0     False   False     False   False         False           False   \n",
       "1     False   False     False   False         False           False   \n",
       "2     False   False     False   False         False           False   \n",
       "3     False   False     False   False         False           False   \n",
       "4     False   False     False   False         False           False   \n",
       "...     ...     ...       ...     ...           ...             ...   \n",
       "4172  False   False     False   False         False           False   \n",
       "4173  False   False     False   False         False           False   \n",
       "4174  False   False     False   False         False           False   \n",
       "4175  False   False     False   False         False           False   \n",
       "4176  False   False     False   False         False           False   \n",
       "\n",
       "      Viscera weight  Shell weight  Rings  \n",
       "0              False         False  False  \n",
       "1              False         False  False  \n",
       "2              False         False  False  \n",
       "3              False         False  False  \n",
       "4              False         False  False  \n",
       "...              ...           ...    ...  \n",
       "4172           False         False  False  \n",
       "4173           False         False  False  \n",
       "4174           False         False  False  \n",
       "4175           False         False  False  \n",
       "4176           False         False  False  \n",
       "\n",
       "[4177 rows x 9 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "651e14f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sex               0\n",
       "Length            0\n",
       "Diameter          0\n",
       "Height            0\n",
       "Whole weight      0\n",
       "Shucked weight    0\n",
       "Viscera weight    0\n",
       "Shell weight      0\n",
       "Rings             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "12074799",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7c96c5e",
   "metadata": {},
   "source": [
    "# outliers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8b3870e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x1e721679820>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(dataset['Sex'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5071ad7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Sex', ylabel='Rings'>"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Sex',y='Rings',data=dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "0c6b1c3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Rings'>"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(y='Rings',data=dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "532793b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9.933684462532918"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset['Rings'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f4c91f70",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "data1=dataset[dataset['Rings']<12]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "16e1532d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Rings'>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(y='Rings',data=data1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e885b4a7",
   "metadata": {},
   "source": [
    "# Categorial Encoding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5223fffd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "      <th>Sex_F</th>\n",
       "      <th>Sex_I</th>\n",
       "      <th>Sex_M</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.455</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.5140</td>\n",
       "      <td>0.2245</td>\n",
       "      <td>0.1010</td>\n",
       "      <td>0.1500</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.350</td>\n",
       "      <td>0.265</td>\n",
       "      <td>0.090</td>\n",
       "      <td>0.2255</td>\n",
       "      <td>0.0995</td>\n",
       "      <td>0.0485</td>\n",
       "      <td>0.0700</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.530</td>\n",
       "      <td>0.420</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.6770</td>\n",
       "      <td>0.2565</td>\n",
       "      <td>0.1415</td>\n",
       "      <td>0.2100</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.440</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.5160</td>\n",
       "      <td>0.2155</td>\n",
       "      <td>0.1140</td>\n",
       "      <td>0.1550</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.330</td>\n",
       "      <td>0.255</td>\n",
       "      <td>0.080</td>\n",
       "      <td>0.2050</td>\n",
       "      <td>0.0895</td>\n",
       "      <td>0.0395</td>\n",
       "      <td>0.0550</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4172</th>\n",
       "      <td>0.565</td>\n",
       "      <td>0.450</td>\n",
       "      <td>0.165</td>\n",
       "      <td>0.8870</td>\n",
       "      <td>0.3700</td>\n",
       "      <td>0.2390</td>\n",
       "      <td>0.2490</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4173</th>\n",
       "      <td>0.590</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.9660</td>\n",
       "      <td>0.4390</td>\n",
       "      <td>0.2145</td>\n",
       "      <td>0.2605</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4174</th>\n",
       "      <td>0.600</td>\n",
       "      <td>0.475</td>\n",
       "      <td>0.205</td>\n",
       "      <td>1.1760</td>\n",
       "      <td>0.5255</td>\n",
       "      <td>0.2875</td>\n",
       "      <td>0.3080</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4175</th>\n",
       "      <td>0.625</td>\n",
       "      <td>0.485</td>\n",
       "      <td>0.150</td>\n",
       "      <td>1.0945</td>\n",
       "      <td>0.5310</td>\n",
       "      <td>0.2610</td>\n",
       "      <td>0.2960</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4176</th>\n",
       "      <td>0.710</td>\n",
       "      <td>0.555</td>\n",
       "      <td>0.195</td>\n",
       "      <td>1.9485</td>\n",
       "      <td>0.9455</td>\n",
       "      <td>0.3765</td>\n",
       "      <td>0.4950</td>\n",
       "      <td>12</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4177 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length  Diameter  Height  Whole weight  Shucked weight  Viscera weight  \\\n",
       "0      0.455     0.365   0.095        0.5140          0.2245          0.1010   \n",
       "1      0.350     0.265   0.090        0.2255          0.0995          0.0485   \n",
       "2      0.530     0.420   0.135        0.6770          0.2565          0.1415   \n",
       "3      0.440     0.365   0.125        0.5160          0.2155          0.1140   \n",
       "4      0.330     0.255   0.080        0.2050          0.0895          0.0395   \n",
       "...      ...       ...     ...           ...             ...             ...   \n",
       "4172   0.565     0.450   0.165        0.8870          0.3700          0.2390   \n",
       "4173   0.590     0.440   0.135        0.9660          0.4390          0.2145   \n",
       "4174   0.600     0.475   0.205        1.1760          0.5255          0.2875   \n",
       "4175   0.625     0.485   0.150        1.0945          0.5310          0.2610   \n",
       "4176   0.710     0.555   0.195        1.9485          0.9455          0.3765   \n",
       "\n",
       "      Shell weight  Rings  Sex_F  Sex_I  Sex_M  \n",
       "0           0.1500     15      0      0      1  \n",
       "1           0.0700      7      0      0      1  \n",
       "2           0.2100      9      1      0      0  \n",
       "3           0.1550     10      0      0      1  \n",
       "4           0.0550      7      0      1      0  \n",
       "...            ...    ...    ...    ...    ...  \n",
       "4172        0.2490     11      1      0      0  \n",
       "4173        0.2605     10      0      0      1  \n",
       "4174        0.3080      9      0      0      1  \n",
       "4175        0.2960     10      1      0      0  \n",
       "4176        0.4950     12      0      0      1  \n",
       "\n",
       "[4177 rows x 11 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_tips=pd.get_dummies(dataset)\n",
    "data_tips"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c3c70a0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one_encde=OneHotEncoder(sparse=False)\n",
    "encoded_arr=one_encde.fit_transform(dataset[['Length','Height','Sex','Diameter']])\n",
    "encoded_arr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5e6ed3b",
   "metadata": {},
   "source": [
    "# Split the data into dependent and independent variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4dd995ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       0.5140\n",
       "1       0.2255\n",
       "2       0.6770\n",
       "3       0.5160\n",
       "4       0.2050\n",
       "         ...  \n",
       "4172    0.8870\n",
       "4173    0.9660\n",
       "4174    1.1760\n",
       "4175    1.0945\n",
       "4176    1.9485\n",
       "Name: Whole weight, Length: 4177, dtype: float64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=dataset.iloc[:,1:4]\n",
    "y=dataset.iloc[:,4]\n",
    "x\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb5af2ff",
   "metadata": {},
   "source": [
    "# Scale the independent variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f7ee787b",
   "metadata": {},
   "outputs": [],
   "source": [
    "independent=dataset.iloc[1:,1:7].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c30afa8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.35  , 0.265 , 0.09  , 0.2255, 0.0995, 0.0485],\n",
       "       [0.53  , 0.42  , 0.135 , 0.677 , 0.2565, 0.1415],\n",
       "       [0.44  , 0.365 , 0.125 , 0.516 , 0.2155, 0.114 ],\n",
       "       ...,\n",
       "       [0.6   , 0.475 , 0.205 , 1.176 , 0.5255, 0.2875],\n",
       "       [0.625 , 0.485 , 0.15  , 1.0945, 0.531 , 0.261 ],\n",
       "       [0.71  , 0.555 , 0.195 , 1.9485, 0.9455, 0.3765]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "independent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f833750f",
   "metadata": {},
   "outputs": [],
   "source": [
    "##Dependent variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9bc20100",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([], shape=(4176, 0), dtype=float64)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dependent=dataset.iloc[1:,9:].values\n",
    "dependent"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df435a7d",
   "metadata": {},
   "source": [
    "# Split the data into training and testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "1d6b0d2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "9c1e1aa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(independent,dependent,test_size=0.2,random_state=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "bb9a2556",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.565 , 0.435 , 0.15  , 0.99  , 0.5795, 0.1825],\n",
       "       [0.48  , 0.37  , 0.125 , 0.5435, 0.244 , 0.101 ],\n",
       "       [0.44  , 0.35  , 0.12  , 0.375 , 0.1425, 0.0965],\n",
       "       ...,\n",
       "       [0.555 , 0.43  , 0.125 , 0.7005, 0.3395, 0.1355],\n",
       "       [0.51  , 0.395 , 0.145 , 0.6185, 0.216 , 0.1385],\n",
       "       [0.595 , 0.47  , 0.155 , 1.2015, 0.492 , 0.3865]])"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "d2b1f0d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.455 , 0.365 , 0.11  , 0.385 , 0.166 , 0.046 ],\n",
       "       [0.47  , 0.37  , 0.18  , 0.51  , 0.1915, 0.1285],\n",
       "       [0.72  , 0.575 , 0.17  , 1.9335, 0.913 , 0.389 ],\n",
       "       ...,\n",
       "       [0.275 , 0.215 , 0.075 , 0.1155, 0.0485, 0.029 ],\n",
       "       [0.39  , 0.3   , 0.09  , 0.252 , 0.1065, 0.053 ],\n",
       "       [0.585 , 0.46  , 0.165 , 1.1135, 0.5825, 0.2345]])"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "fb523f9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([], shape=(3340, 0), dtype=float64)"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "89bc6e51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([], shape=(836, 0), dtype=float64)"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63d9eaaa",
   "metadata": {},
   "source": [
    "# Build the Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "d2cc1268",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import datasets\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.datasets import make_classification\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "65062a14",
   "metadata": {},
   "outputs": [],
   "source": [
    "iris=datasets.load_iris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "e17547e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']\n"
     ]
    }
   ],
   "source": [
    "print(iris.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "8bf82792",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['setosa' 'versicolor' 'virginica']\n"
     ]
    }
   ],
   "source": [
    "print(iris.target_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "0554300b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5.1, 3.5, 1.4, 0.2],\n",
       "       [4.9, 3. , 1.4, 0.2],\n",
       "       [4.7, 3.2, 1.3, 0.2],\n",
       "       [4.6, 3.1, 1.5, 0.2],\n",
       "       [5. , 3.6, 1.4, 0.2],\n",
       "       [5.4, 3.9, 1.7, 0.4],\n",
       "       [4.6, 3.4, 1.4, 0.3],\n",
       "       [5. , 3.4, 1.5, 0.2],\n",
       "       [4.4, 2.9, 1.4, 0.2],\n",
       "       [4.9, 3.1, 1.5, 0.1],\n",
       "       [5.4, 3.7, 1.5, 0.2],\n",
       "       [4.8, 3.4, 1.6, 0.2],\n",
       "       [4.8, 3. , 1.4, 0.1],\n",
       "       [4.3, 3. , 1.1, 0.1],\n",
       "       [5.8, 4. , 1.2, 0.2],\n",
       "       [5.7, 4.4, 1.5, 0.4],\n",
       "       [5.4, 3.9, 1.3, 0.4],\n",
       "       [5.1, 3.5, 1.4, 0.3],\n",
       "       [5.7, 3.8, 1.7, 0.3],\n",
       "       [5.1, 3.8, 1.5, 0.3],\n",
       "       [5.4, 3.4, 1.7, 0.2],\n",
       "       [5.1, 3.7, 1.5, 0.4],\n",
       "       [4.6, 3.6, 1. , 0.2],\n",
       "       [5.1, 3.3, 1.7, 0.5],\n",
       "       [4.8, 3.4, 1.9, 0.2],\n",
       "       [5. , 3. , 1.6, 0.2],\n",
       "       [5. , 3.4, 1.6, 0.4],\n",
       "       [5.2, 3.5, 1.5, 0.2],\n",
       "       [5.2, 3.4, 1.4, 0.2],\n",
       "       [4.7, 3.2, 1.6, 0.2],\n",
       "       [4.8, 3.1, 1.6, 0.2],\n",
       "       [5.4, 3.4, 1.5, 0.4],\n",
       "       [5.2, 4.1, 1.5, 0.1],\n",
       "       [5.5, 4.2, 1.4, 0.2],\n",
       "       [4.9, 3.1, 1.5, 0.2],\n",
       "       [5. , 3.2, 1.2, 0.2],\n",
       "       [5.5, 3.5, 1.3, 0.2],\n",
       "       [4.9, 3.6, 1.4, 0.1],\n",
       "       [4.4, 3. , 1.3, 0.2],\n",
       "       [5.1, 3.4, 1.5, 0.2],\n",
       "       [5. , 3.5, 1.3, 0.3],\n",
       "       [4.5, 2.3, 1.3, 0.3],\n",
       "       [4.4, 3.2, 1.3, 0.2],\n",
       "       [5. , 3.5, 1.6, 0.6],\n",
       "       [5.1, 3.8, 1.9, 0.4],\n",
       "       [4.8, 3. , 1.4, 0.3],\n",
       "       [5.1, 3.8, 1.6, 0.2],\n",
       "       [4.6, 3.2, 1.4, 0.2],\n",
       "       [5.3, 3.7, 1.5, 0.2],\n",
       "       [5. , 3.3, 1.4, 0.2],\n",
       "       [7. , 3.2, 4.7, 1.4],\n",
       "       [6.4, 3.2, 4.5, 1.5],\n",
       "       [6.9, 3.1, 4.9, 1.5],\n",
       "       [5.5, 2.3, 4. , 1.3],\n",
       "       [6.5, 2.8, 4.6, 1.5],\n",
       "       [5.7, 2.8, 4.5, 1.3],\n",
       "       [6.3, 3.3, 4.7, 1.6],\n",
       "       [4.9, 2.4, 3.3, 1. ],\n",
       "       [6.6, 2.9, 4.6, 1.3],\n",
       "       [5.2, 2.7, 3.9, 1.4],\n",
       "       [5. , 2. , 3.5, 1. ],\n",
       "       [5.9, 3. , 4.2, 1.5],\n",
       "       [6. , 2.2, 4. , 1. ],\n",
       "       [6.1, 2.9, 4.7, 1.4],\n",
       "       [5.6, 2.9, 3.6, 1.3],\n",
       "       [6.7, 3.1, 4.4, 1.4],\n",
       "       [5.6, 3. , 4.5, 1.5],\n",
       "       [5.8, 2.7, 4.1, 1. ],\n",
       "       [6.2, 2.2, 4.5, 1.5],\n",
       "       [5.6, 2.5, 3.9, 1.1],\n",
       "       [5.9, 3.2, 4.8, 1.8],\n",
       "       [6.1, 2.8, 4. , 1.3],\n",
       "       [6.3, 2.5, 4.9, 1.5],\n",
       "       [6.1, 2.8, 4.7, 1.2],\n",
       "       [6.4, 2.9, 4.3, 1.3],\n",
       "       [6.6, 3. , 4.4, 1.4],\n",
       "       [6.8, 2.8, 4.8, 1.4],\n",
       "       [6.7, 3. , 5. , 1.7],\n",
       "       [6. , 2.9, 4.5, 1.5],\n",
       "       [5.7, 2.6, 3.5, 1. ],\n",
       "       [5.5, 2.4, 3.8, 1.1],\n",
       "       [5.5, 2.4, 3.7, 1. ],\n",
       "       [5.8, 2.7, 3.9, 1.2],\n",
       "       [6. , 2.7, 5.1, 1.6],\n",
       "       [5.4, 3. , 4.5, 1.5],\n",
       "       [6. , 3.4, 4.5, 1.6],\n",
       "       [6.7, 3.1, 4.7, 1.5],\n",
       "       [6.3, 2.3, 4.4, 1.3],\n",
       "       [5.6, 3. , 4.1, 1.3],\n",
       "       [5.5, 2.5, 4. , 1.3],\n",
       "       [5.5, 2.6, 4.4, 1.2],\n",
       "       [6.1, 3. , 4.6, 1.4],\n",
       "       [5.8, 2.6, 4. , 1.2],\n",
       "       [5. , 2.3, 3.3, 1. ],\n",
       "       [5.6, 2.7, 4.2, 1.3],\n",
       "       [5.7, 3. , 4.2, 1.2],\n",
       "       [5.7, 2.9, 4.2, 1.3],\n",
       "       [6.2, 2.9, 4.3, 1.3],\n",
       "       [5.1, 2.5, 3. , 1.1],\n",
       "       [5.7, 2.8, 4.1, 1.3],\n",
       "       [6.3, 3.3, 6. , 2.5],\n",
       "       [5.8, 2.7, 5.1, 1.9],\n",
       "       [7.1, 3. , 5.9, 2.1],\n",
       "       [6.3, 2.9, 5.6, 1.8],\n",
       "       [6.5, 3. , 5.8, 2.2],\n",
       "       [7.6, 3. , 6.6, 2.1],\n",
       "       [4.9, 2.5, 4.5, 1.7],\n",
       "       [7.3, 2.9, 6.3, 1.8],\n",
       "       [6.7, 2.5, 5.8, 1.8],\n",
       "       [7.2, 3.6, 6.1, 2.5],\n",
       "       [6.5, 3.2, 5.1, 2. ],\n",
       "       [6.4, 2.7, 5.3, 1.9],\n",
       "       [6.8, 3. , 5.5, 2.1],\n",
       "       [5.7, 2.5, 5. , 2. ],\n",
       "       [5.8, 2.8, 5.1, 2.4],\n",
       "       [6.4, 3.2, 5.3, 2.3],\n",
       "       [6.5, 3. , 5.5, 1.8],\n",
       "       [7.7, 3.8, 6.7, 2.2],\n",
       "       [7.7, 2.6, 6.9, 2.3],\n",
       "       [6. , 2.2, 5. , 1.5],\n",
       "       [6.9, 3.2, 5.7, 2.3],\n",
       "       [5.6, 2.8, 4.9, 2. ],\n",
       "       [7.7, 2.8, 6.7, 2. ],\n",
       "       [6.3, 2.7, 4.9, 1.8],\n",
       "       [6.7, 3.3, 5.7, 2.1],\n",
       "       [7.2, 3.2, 6. , 1.8],\n",
       "       [6.2, 2.8, 4.8, 1.8],\n",
       "       [6.1, 3. , 4.9, 1.8],\n",
       "       [6.4, 2.8, 5.6, 2.1],\n",
       "       [7.2, 3. , 5.8, 1.6],\n",
       "       [7.4, 2.8, 6.1, 1.9],\n",
       "       [7.9, 3.8, 6.4, 2. ],\n",
       "       [6.4, 2.8, 5.6, 2.2],\n",
       "       [6.3, 2.8, 5.1, 1.5],\n",
       "       [6.1, 2.6, 5.6, 1.4],\n",
       "       [7.7, 3. , 6.1, 2.3],\n",
       "       [6.3, 3.4, 5.6, 2.4],\n",
       "       [6.4, 3.1, 5.5, 1.8],\n",
       "       [6. , 3. , 4.8, 1.8],\n",
       "       [6.9, 3.1, 5.4, 2.1],\n",
       "       [6.7, 3.1, 5.6, 2.4],\n",
       "       [6.9, 3.1, 5.1, 2.3],\n",
       "       [5.8, 2.7, 5.1, 1.9],\n",
       "       [6.8, 3.2, 5.9, 2.3],\n",
       "       [6.7, 3.3, 5.7, 2.5],\n",
       "       [6.7, 3. , 5.2, 2.3],\n",
       "       [6.3, 2.5, 5. , 1.9],\n",
       "       [6.5, 3. , 5.2, 2. ],\n",
       "       [6.2, 3.4, 5.4, 2.3],\n",
       "       [5.9, 3. , 5.1, 1.8]])"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris.data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "824b7342",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
       "       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
       "       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
       "       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "70d49263",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=iris.data\n",
    "y=iris.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "64bba674",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(150, 4)"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "ffc49e97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(150,)"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "e07adb2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "clf=RandomForestClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "a594decc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.fit(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "47481487",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.09934163 0.02933361 0.41455791 0.45676685]\n"
     ]
    }
   ],
   "source": [
    "print(clf.feature_importances_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "9ae69a83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5.1, 3.5, 1.4, 0.2])"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "45233ba9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0]\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict([[5.1, 3.5, 1.4, 0.2]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "e9768503",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0]\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict(x[[0]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "7c65d9bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict_proba(x[[0]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "94ce43b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.fit(iris.data,iris.target_names[iris.target])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eedef4f3",
   "metadata": {},
   "source": [
    "# Train & Test the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "ed373778",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "fcd7c700",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((120, 4), (120,))"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape,y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "12e3dd27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((30, 4), (30,))"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "ce84ce3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "7fae403c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0]\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict([[5.1, 3.5, 1.4, 0.2]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "ef217ebc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict_proba([[5.1, 3.5, 1.4, 0.2]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "19c8da33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 2 0 2 2 0 2 0 2 1 1 2 1 1 2 2 1 1 0 2 2 0 0 1 2 1 0 0 2 0]\n"
     ]
    }
   ],
   "source": [
    "print(clf.predict(x_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "58d17ed6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 2 0 2 2 0 2 0 2 1 1 2 1 1 2 2 1 1 0 2 2 0 0 1 2 1 0 0 2 0]\n"
     ]
    }
   ],
   "source": [
    "print(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "48a02369",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n"
     ]
    }
   ],
   "source": [
    "print(clf.score(x_test,y_test))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}