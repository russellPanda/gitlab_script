# gitlab_script





1. 使用脚本获取帐号能拿到的项目的地址和分支
2. 使用shell脚本进行迁移仓库

	```bash
	syncgit(){
	  rm -rf $workdir/${repo_name}
	  cd $workdir
	  git clone http://guest_dfzq:'DFzq001!*Devops888'@58.210.154.140:8888/DFZQ2-Devops/${repo_name}.git
	
	  cd $workdir/${repo_name}
	  git checkout $refspec
	  git branch -D master
	  git checkout -b master # 用当前的分支创建master分支
	  git remote set-url origin http://devops-mayunhao:yi0305ha@git.orientsec.com.cn/scm/devops/${dest_repo}.git
	  git push  -f -u origin master
	}
	```



ps:
> 直接使用git命令
>
> ```bash
> git clone --bare http://10.10.32.97:8788/root/before1-private.git
> cd before1-private.git/
> git push --mirror http://10.10.32.97:8788/root/before1-private-push.git
