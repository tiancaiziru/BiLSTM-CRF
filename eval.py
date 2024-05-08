import os

def conlleval(label_predict, label_path, metric_path):
    eval_perl = "D:/zh-NER-TF-master/zh-NER-TF-master/conlleval.pl"  # Change this line to the path of conlleval.pl
    with open(label_path, "w", encoding="utf-8") as fw:
        line = []
        for sent_result in label_predict:
            for char, tag, tag_ in sent_result:
                tag = '0' if tag == 'O' else tag
                char = char.encode("utf-8")
                line.append("{} {} {}\n".format(char, tag, tag_))
            line.append("\n")
        fw.writelines(line)
    os.system("perl {} < {} > {}".format(eval_perl, label_path, metric_path))
    with open(metric_path, encoding="utf-8") as fr:
        metrics = [line.strip() for line in fr]
    return metrics
