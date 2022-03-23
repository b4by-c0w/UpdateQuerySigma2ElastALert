# UpdateQuerySigma2ElastALert
This script use to update query from rule which write sigma format to elastalert and backup old rule with sigma tools.


**How to use**

Install requirement lib

python -m pip install -r requirement.txt

Set path of sigma tools. Download it from [here](https://github.com/SigmaHQ/sigma)

python .\UpdateQueryRule.py -o '.\file_need_to_update.yml' -n '.\file_sigma_rule_use_for_updateyml'                                        

If succcessfull, you see
![image](https://user-images.githubusercontent.com/79184015/148478408-1a969334-9dc7-463c-aa05-e5f451cf4c93.png)
