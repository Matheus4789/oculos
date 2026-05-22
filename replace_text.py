import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles and meta
content = content.replace('Ray-Ban Wayfarer Folding Classic RB4105 - Original | E&M Glasses (Revendedor Autorizado)', 'Óculos E&M Folding Classic | Edição Original Dobrável')
content = content.replace('Ray-Ban Wayfarer Folding Classic RB4105 100% original na E&M Glasses, revendedor autorizado Ray-Ban.', 'Óculos E&M Folding Classic 100% original na E&M Glasses.')
content = content.replace('Ray-Ban Wayfarer Folding Classic', 'Óculos E&M Folding Classic')
content = content.replace('RB4105', 'Edição Dobrável')
content = content.replace('Ray-Ban Wayfarer Folding', 'Óculos E&M Folding')

# Other generic replacements
content = content.replace('Ray-Ban', 'E&M Glasses')
content = content.replace('Wayfarer', 'Folding Classic')

# Specific string fixes that might sound weird after replacement
content = content.replace('100% Original E&M Glasses', '100% Original')
content = content.replace('Produto E&M Glasses 100% Original', 'Produto 100% Original')
content = content.replace('revendedor autorizado E&M Glasses', 'loja oficial')
content = content.replace('revendedor autorizado oficial', 'loja oficial')
content = content.replace('Garantia de fábrica E&M Glasses', 'Garantia de fábrica')
content = content.replace('Garantia Oficial E&M Glasses', 'Garantia Oficial')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

