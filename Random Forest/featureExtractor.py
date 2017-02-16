"""
Data Mining Final Project. Product Search Relevance for Home Depot from Kaggle

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Create new features
@version    : uses Python 3.4.3
"""

"import libraries"
import common as cm


def createFeatures(combined):
	''' Features on product Information'''
    combined['product_info'] = combined['search_term']+"\t"+combined['product_title'] +"\t"+combined['product_description']
    
    ''' Features on the total length of query'''
    combined['len_of_query'] = combined['search_term'].map(lambda word:len(word.split())).astype(np.int64)
    
    ''' Features on total length of product title'''
    combined['len_of_title'] = combined['product_title'].map(lambda word:len(word.split())).astype(np.int64)
    
    ''' Features on total length of product description'''
    combined['len_of_description'] = combined['product_description'].map(lambda word:len(word.split())).astype(np.int64)
    
    ''' Features on total length of brand Information'''
    combined['len_of_brand'] = combined['brand'].map(lambda word:len(word.split())).astype(np.int64)
    
    ''' Features on the queried search term'''
    combined['search_term'] = combined['product_info'].map(lambda word:cm.GetRootWords(word.split('\t')[0],word.split('\t')[1]))
    
    ''' Features on title contained in query'''
    combined['query_in_title'] = combined['product_info'].map(lambda word:cm.countOccurence(word.split('\t')[0],word.split('\t')[1],0))
    
    ''' Features on description of the query'''
    combined['query_in_description'] = combined['product_info'].map(lambda word:cm.countOccurence(word.split('\t')[0],word.split('\t')[2],0))
    
    ''' Features on the stop word of the title'''
    combined['query_last_word_in_title'] = combined['product_info'].map(lambda word:cm.findCommonWord(word.split('\t')[0].split(" ")[-1],word.split('\t')[1]))
    
    ''' eatures on the stop word of the title'''
    combined['query_last_word_in_description'] = combined['product_info'].map(lambda word:cm.findCommonWord(word.split('\t')[0].split(" ")[-1],word.split('\t')[2]))
    
    ''' Features on word present in the title'''
    combined['word_in_title'] = combined['product_info'].map(lambda word:cm.findCommonWord(word.split('\t')[0],word.split('\t')[1]))
    
    ''' Features on word present in the description'''
    combined['word_in_description'] = combined['product_info'].map(lambda word:cm.findCommonWord(word.split('\t')[0],word.split('\t')[2]))
    
    ''' Features on the ratio of title'''
    combined['ratio_title'] = combined['word_in_title']/combined['len_of_query']
    
    ''' Features on ration description'''
    combined['ratio_description'] = combined['word_in_description']/combined['len_of_query']
   
	''' Features on attribute of the search term'''
    combined['attr'] = combined['search_term']+"\t"+combined['brand']
    
    ''' Features on total word present in the brand Information'''
	combined['word_in_brand'] = combined['attr'].map(lambda word:cm.findCommonWord(word.split('\t')[0],word.split('\t')[1]))
    
    ''' Features on ratio of the brand description'''
    combined['ratio_brand'] = combined['word_in_brand']/combined['len_of_brand']
    
    ''' Now create unique brand information '''
    combinedBrand = pd.unique(combined.brand.ravel())

	return combined
