import json
#f=open('/scratch/tocho_root/tocho0/yiweilyu/diffuseq_TPA_h128_lr0.0001_t1000_sqrt_lossaware_seed102_TPA20221202-17:31:46')
#f = open('../generation_outputs/diffuseq_SBR_h128_lr0.0001_t1000_sqrt_lossaware_seed102_SBR20221205-11:27:05/ema_0.9999_008000.pt.samples/seed132_step0.json')
#f = open('../generation_outputs/diffuseq_AEM_h128_lr0.0001_t1000_sqrt_lossaware_seed102_AEM20221203-02:30:54/ema_0.9999_040000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_ARR_h128_lr0.0001_t1000_sqrt_lossaware_seed103_ARR20221205-17:11:46/ema_0.9999_032000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_PPR_h128_lr1e-05_t1000_sqrt_lossaware_seed103_PPR20221205-17:05:43/ema_0.9999_034000.pt.samples/seed123_step0.json')
#f=open('generation_outputs/diffuseq_PP_Front_Back_ADJADV_Removal_h128_lr0.0001_t1000_sqrt_lossaware_seed102_PP_Front_Back_ADJADV_Removal20221205-13:24:38/ema_0.9999_010000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_IAD_h128_lr0.0001_t1000_sqrt_lossaware_seed103_IAD20221206-14:56:44/ema_0.9999_030000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_PPR_h128_lr1e-05_t1000_sqrt_lossaware_seed103_PPR20221207-12:46:43/ema_0.9999_050000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_single_fusion_h128_lr0.0001_t1000_sqrt_lossaware_seed102_single_fusion20221206-21:31:40/ema_0.9999_052000.pt.samples/seed123_step0.json')
#f=open('../generation_outputs/diffuseq_SBR_h128_lr1e-05_t1000_sqrt_lossaware_seed103_SBR20221208-18:04:16/ema_0.9999_050000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_VEM_h128_lr1e-05_t1000_sqrt_lossaware_seed103_VEM20221209-17:17:49/ema_0.9999_036000.pt.samples/seed132_step0.json')
#f=open('../generation_outputs/diffuseq_PFB_h128_lr1e-05_t1000_sqrt_lossaware_seed103_PFB20221210-20:02:51/ema_0.9999_050000.pt.samples/seed132_step0.json')
f=open('../generation_outputs/diffuseq_EMFTI_h128_lr1e-05_t1000_sqrt_lossaware_seed103_EMFTI20230111-17:39:51/ema_0.9999_100000.pt.samples/seed132_step0.json')

lines = f.readlines()
"""
for i in range(1,4):
    for j in range(5,6):
        g1 = open('../hyp'+str(i)+str(j)+'.txt','w+')
        g2 = open('../ref'+str(i)+str(j)+'.txt','w+')
        for line in lines:
            d = json.loads(line)
            if d['source'][6] == str(i) and d['source'][8] == str(j):
                g1.write(d['recover'][6:-6]+'\n')
                g2.write(d['reference'][6:-6]+'\n')
        g1.close()
        g2.close()
"""
"""
for i in range(0,13):
    g1 = open('../hyp'+str(i)+'.txt','w+')
    g2 = open('../ref'+str(i)+'.txt','w+')

    for line in lines:
        d = json.loads(line)
        if d['source'][6:6+len(str(i))] == str(i):
            g1.write(d['recover'][6:-6]+'\n')
            g2.write(d['reference'][6:-6]+'\n')
    g1.close()
    g2.close()
"""

g1 = open('../hyp.txt','w+')
g2 = open('../ref.txt','w+')

for line in lines:
    d = json.loads(line)
    g1.write(d['recover'][6:-6]+'\n')
    g2.write(d['reference'][6:-6]+'\n')
g1.close()
g2.close()
f.close()
