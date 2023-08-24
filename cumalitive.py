import matplotlib.pyplot as plt

# Given data in dictionary form
data1 = {"5":316,"6":576,"7":866,"8":1153,"9":1450,"10":1882,"11":2359,"12":2703,"13":3171,"14":3573,"15":4224,"16":5027,"17":5575,"18":6263,"19":6968,"20":7424,"21":8185,"22":8738,"23":9374,"24":9950,"25":10581,"26":10796,"27":10959,"28":10995,"29":11146,"30":11351,"31":11218,"32":11178,"33":10874,"34":10701,"35":10595,"36":10106,"37":9325,"38":8723,"39":8156,"40":7436,"41":6948,"42":6298,"43":5540,"44":4785,"45":4284,"46":3629,"47":3171,"48":2728,"49":2391,"50":1852,"51":1525,"52":1160,"53":886,"54":576,"55":310}


data2 = {"5":316,"6":892,"7":1758,"8":2911,"9":4361,"10":6243,"11":8602,"12":11305,"13":14476,"14":18049,"15":22273,"16":27300,"17":32875,"18":39138,"19":46106,"20":53530,"21":61715,"22":70453,"23":79827,"24":89777,"25":100358,"26":111154,"27":122113,"28":133108,"29":144254,"30":155605,"31":166823,"32":178001,"33":188875,"34":199576,"35":210171,"36":220277,"37":229602,"38":238325,"39":246481,"40":253917,"41":260865,"42":267163,"43":272703,"44":277488,"45":281772,"46":285401,"47":288572,"48":291300,"49":293691,"50":295543,"51":297068,"52":298228,"53":299114,"54":299690,"55":300000}

# Extract values and their frequencies for both datasets
values1 = [int(key) for key in data1.keys()]
frequencies1 = list(data1.values())

values2 = [int(key) for key in data2.keys()]
frequencies2 = list(data2.values())

# Create subplots with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Create the first histogram on the first subplot
ax1.bar(values1, frequencies1, align='center', alpha=0.5, color='blue', width=1)
ax1.set_xlabel('Minutes past 8')
ax1.set_ylabel('Frequency')
ax1.set_title('Rate Of Children Arriving')

# Create the second histogram on the second subplot
ax2.bar(values2, frequencies2, align='center', alpha=0.5, color='red', width=1)
ax2.set_xlabel('Minutes past 8')
ax2.set_ylabel('Frequency')
ax2.set_title('Cumalative # Of Students Present')

# Adjust the layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()