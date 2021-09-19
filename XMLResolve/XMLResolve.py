# -*- coding: utf-8 -*-
"""
    @Author  : Wangxiaoyao
    @Time    : 2021/09/19
    @Comment : 解析XML
"""

import pandas as pd

# 存储数据的列表
tableListDom = []
tableListElement = []

# 方法1: 使用dom方式解析
from xml.dom.minidom import parse
def readXMLAccordingToDom():
    # 步骤1：传入路径
	domTree = parse("G:/Code/branch_python/XMLResolve/misc.xml")
	# 步骤2：文档根元素
	rootNode = domTree.documentElement
	print(rootNode.nodeName)
	# 步骤3：属性信息
	components = rootNode.getElementsByTagName("component")
	# 步骤4：获取特征中属性
	for component in components:
		if component.hasAttribute("name"):
			# 特征值
			#print("name:", customer.getAttribute("name"))
			name = component.getAttribute("name")
			# 属性值
			options = component.getElementsByTagName("option")
			for option in options:
				#print("type:", option.getAttribute("type"))
				type = option.getAttribute("type")

				table = [name, type]
				tableListDom.append(table)

# 方法2：使用elementtree解析
import xml.etree.ElementTree as ET
def readXMLAccordingToElement():
	# 步骤1：传入路径
	tree = ET.parse("G:/Code/branch_python/XMLResolve/misc.xml")
	# 步骤1：文档根元素
	root = tree.getroot()
	#print('root_tag:', root.tag)
	# 步骤3：获取特征中属性
	for component in root:
		# 特征值
		print("component_name:", component.attrib["name"])
		name = component.attrib['name']
		# 属性值
		for option in component:
			print("option_type:", option.attrib["type"])
			type = option.attrib['type']

			table = [name, type]
			tableListElement.append(table)

if __name__ == '__main__':
	# 方法1: 使用Dom
	print('方法1: 使用Dom')
	readXMLAccordingToDom()
	print(tableListDom)

	# 方法2： 使用Element
	print('方法2： 使用Element')
	readXMLAccordingToElement();
	print(tableListElement)

	dataframe = pd.DataFrame(tableListElement)
	dataframe.columns = ['d1', 'd2']
	print(dataframe)
	dataframe.to_excel('G:/Code/branch_python/XMLResolve/list.xls')
