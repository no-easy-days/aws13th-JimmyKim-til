# 이 파일에서 디렉토리 2개에 선언했던 vpc 모듈을 호출하고, eks 모듈을 호출한다.
# 모듈별로 terraform apply를 했다면, 여기서 각 모듈을 전부 컨트롤할 것이기 때문에 terraform destroy가 선행되어야 함.
# 똑같이 프로바이더를 선언해주고 모듈을 불러오도록 코드를 짠다.
provider "aws" {
    region = "ap-northeast-2"
}
# 프로바이더 선언

module "eks-vpc-terraform" {
    source = "./vpc"  
}
# vpc 모듈 불러오기

module "eks-cluster-terraform" {
    source = "./eks"
    eks-vpc-id = module.eks-vpc-terraform.eks-vpc-id
    prv-sub1-id = module.eks-vpc-terraform.prv-sub1-id
    prv-sub2-id = module.eks-vpc-terraform.prv-sub2-id
    pub-sub1-id = module.eks-vpc-terraform.prv-sub1-id
    pub-sub2-id = module.eks-vpc-terraform.prv-sub2-id
    # eks 모듈 안에 선언하지 않았던 variables.tf의 Value값을 여기서 선언한다!
}
# vpc 모듈 불러오기