from DREAMwalk.generate_similarity_net import save_sim_graph
from DREAMwalk.generate_embeddings import save_embedding_files
from DREAMwalk.predict_associations import predict_dda

if __name__ == '__main__':

    networkf='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/demo_graph.txt'
    hierf='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/demo_hierarchy.csv'
    simf='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/demo_similarty_graph.txt'
    cutoff=0.4

    save_sim_graph(networkf=networkf,hierf=hierf,outputf=simf,cutoff=cutoff)



    # node type file should be given for application of heterogeneous Skip-gram
    nodetypef='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/demo_nodetypes.tsv'
    embeddingf='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/embedding_file.pkl' 

    save_embedding_files(netf=networkf,sim_netf=simf, outputf=embeddingf,
                        nodetypef=nodetypef,tp_factor=0.3)



    pairf='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/demo_dda.tsv'
    modelf='D:/项目/量子随机游走与药物重定位/文章代码/DREAMwalk-main/demo/clf.pkl'

    predict_dda(embeddingf=embeddingf, pairf=pairf, modelf=modelf)