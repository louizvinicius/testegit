import xml.etree.ElementTree as ET

class NotaFiscal:
    def __init__(self, emitente, destinatario, produtos):
        self.emitente = emitente
        self.destinatario = destinatario
        self.produtos = produtos

    def gerar_nfe(self):
        root = ET.Element("NFe")
        # Adicionar elementos à NF-e
        ET.SubElement(root, "emitente").text = self.emitente
        ET.SubElement(root, "destinatario").text = self.destinatario
        produtos_element = ET.SubElement(root, "produtos")
        for produto in self.produtos:
            produto_element = ET.SubElement(produtos_element, "produto")
            ET.SubElement(produto_element, "descricao").text = produto["descricao"]
            ET.SubElement(produto_element, "quantidade").text = produto["quantidade"]
            ET.SubElement(produto_element, "valor").text = produto["valor"]
        #...
        return 0

# Exemplo de uso
emitente = "Empresa XYZ"
destinatario = "Cliente ABC"
produtos = [
    {"descricao": "Produto 1", "quantidade": 2, "valor": 10.99},
    {"descricao": "Produto 2", "quantidade": 3, "valor": 5.99},
]

nfe = NotaFiscal(emitente, destinatario, produtos)
xml_nfe = nfe.gerar_nfe()
print(xml_nfe)