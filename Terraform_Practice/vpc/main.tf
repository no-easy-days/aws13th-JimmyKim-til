# ---- 전역 설정 ----
terraform {
    required_providers {
    # 프로바이더 => 상호 작용할 CSP 인프라 종류. AWS, GCP, Azure 등등...
        aws = {
            source = "hashicorp/aws"
            version = ">= 4.0"
            # 테라폼 프로바이더 모듈의 버전. 다른 모듈이랑 호환 문제 발생할 수 있다. 버전 확인 잘하기.
        }
    }
}

# ---- AWS VPC 생성 ----
resource "aws_vpc" "this" {
# 리소스 이름(this) : 테라폼 상에서의 이름. (참조하기 편한 이름으로 지정하자)
    cidr_block = "10.10.0.0/16"
    enable_dns_support = true
    enable_dns_hostnames = true
    tags = {
        Name = "eks-vpc-terraform"
    }
 }

# ---- IGW 생성 ----
resource "aws_internet_gateway" "this" {
    vpc_id = aws_vpc.this.id
    # 여기서 위에 만든 이름을 바탕으로 리소스 참조를 한다.

    tags = {
        Name = "igw-eks-vpc-terraform"
    }
}

# ---- Subnet 생성 ---- 
resource "aws_subnet" "pub_sub1" {
    vpc_id = aws_vpc.this.id
    cidr_block = "10.10.1.0/24"
    # 당연히, 위에서 만든 vpc cidr block 내에 있어야 함
    availability_zone = "ap-northeast-2a"
    map_public_ip_on_launch = true
    # 퍼블릭 IP 자동 할당
    enable_resource_name_dns_a_record_on_launch = true
    # DNS A Record 활성화

    depends_on = [ aws_internet_gateway.this ]
    # IGW가 만들어지고 나서 만들겠다. DockerCompose.yaml과 유사함

    tags = {
        Name = "eks-vpc-terraform-pub-sub1"
    }
}

resource "aws_subnet" "pub_sub2" {
    vpc_id = aws_vpc.this.id
    cidr_block = "10.10.11.0/24"
    # 당연히, 위에서 만든 vpc cidr block 내에 있어야 함
    availability_zone = "ap-northeast-2c"
    map_public_ip_on_launch = true
    # 퍼블릭 IP 자동 할당
    enable_resource_name_dns_a_record_on_launch = true
    # DNS A Record 활성화

    depends_on = [ aws_internet_gateway.this ]
    # IGW가 만들어지고 나서 만들겠다. DockerCompose.yaml과 유사함

    tags = {
        Name = "eks-vpc-terraform-pub-sub2"
    }
}

resource "aws_subnet" "prv_sub1" {
    vpc_id = aws_vpc.this.id
    cidr_block = "10.10.2.0/24"
    # 당연히, 위에서 만든 vpc cidr block 내에 있어야 함
    availability_zone = "ap-northeast-2a"
    tags = {
        Name = "eks-vpc-terraform-prv-sub1"
    }
}

resource "aws_subnet" "prv_sub2" {
    vpc_id = aws_vpc.this.id
    cidr_block = "10.10.22.0/24"
    # 당연히, 위에서 만든 vpc cidr block 내에 있어야 함
    availability_zone = "ap-northeast-2c"
    tags = {
        Name = "eks-vpc-terraform-prv-sub2"
    }
}

# ---- 라우팅 테이블 생성 ---- 
resource "aws_route_table" "public_rt" {
    vpc_id = aws_vpc.this.id
    route {
        cidr_block = "10.10.0.0/16"
        gateway_id = "local"
    }
    # VPC 내부 서브넷 라우팅
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.this.id
    }
    # 외부로 나가는 서브넷 라우팅
    tags = {
      Name = "pub-rt-eks-vpc-terraform"
    }
}

resource "aws_route_table" "private_rt" {
    vpc_id = aws_vpc.this.id
    route {
        cidr_block = "10.10.0.0/16"
        gateway_id = "local"
        #Next Hop, 내부망
    }
    # VPC 내부 서브넷 라우팅
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_nat_gateway.this.id
    }
    # NAT GW 추가에 따른 프라이빗 서브넷 라우팅 테이블에 추가해주는 설정
    tags = {
      Name = "prv-rt-eks-vpc-terraform"
    }
}

# --- 라우팅 테이블 ~ 서브넷 Association 설정
resource "aws_route_table_association" "pub1_rt_associate" {
    subnet_id = aws_subnet.pub_sub1.id
    # associate 할건데 대상은 퍼블릭 1
    route_table_id = aws_route_table.public_rt.id
    # 라우팅 테이블은 public_rt 쓰기
}

resource "aws_route_table_association" "pub2_rt_associate" {
    subnet_id = aws_subnet.pub_sub2.id
    route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "prv1_rt_associate" {
    subnet_id = aws_subnet.prv_sub1.id
    route_table_id = aws_route_table.private_rt.id
}

resource "aws_route_table_association" "prv2_rt_associate" {
    subnet_id = aws_subnet.prv_sub2.id
    route_table_id = aws_route_table.private_rt.id
}

# EIP 생성 (NAT Gateway 만들기 위해서. 이름만 지정하면된다)
resource "aws_eip" "this" {
    tags = {
      Name = "eip-eks-vpc-terraform"
    }
}

# NAT Gateway 생성
resource "aws_nat_gateway" "this" {
    subnet_id = aws_subnet.pub_sub1.id
    # 퍼블릭 서브넷에 설정
    allocation_id = aws_eip.this.id
    tags = {
      Name = "natgw-eks-vpc-terraform"
    }
}

# Security Group 생성
resource "aws_security_group" "sg-pub" {
    vpc_id = aws_vpc.this.id
    tags = {
      Name = "sg-pub-eks-vpc-terraform"
    }
}

# Security Group의 세부 Rule 생성 
resource "aws_security_group_rule" "http-inbound" {
    type = "ingress"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    # 대괄호는 테라폼에서 정해둔 규칙이기 때문에, 따라가야함.
    security_group_id = aws_security_group.sg-pub.id
}

resource "aws_security_group_rule" "ssh-inbound" {
    type = "ingress"
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    security_group_id = aws_security_group.sg-pub.id
}

resource "aws_security_group_rule" "all-traffic-outbound" {
    type = "egress"
    from_port = 0
    to_port = 0
    # 0 : 포트 한정, 모든 포트를 뜻한다.
    protocol = "-1"
    # -1 : 프로토콜 한정, 모든 프로토콜을 뜻한다.
    cidr_blocks = ["0.0.0.0/0"]
    security_group_id = aws_security_group.sg-pub.id
}
# 테라폼으로 만들면 아웃바운드 Security Group도 명시해서 만들어야한다. 자동으로 만들어지지 않는다.

