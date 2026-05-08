# main에다가 vpc, eks, ec2 이런 식으로 다 만드는 것도 가능하지만, 코드가 점점 확장할수록 에러 발생률이 증가한다.
# 그렇기 때문에, 필요한 AWS 서비스 마다 모듈을 쪼개서 만드는 게 좋다. 응집도(Cohesion)을 높이고 결합도(Coupling)를 낮추자.
# 다른 모듈에서 내가 가진 모듈의 value 값들이 필요할 수 있으므로, "참조"할 수 있게 outputs.tf로 선언해준다.
# 이 폴더에서는 "vpc와 관련된 것"만 선언해줄 수 있다.

output "eks-vpc-id" {
    value = aws_vpc.this.id
}
# eks-vpc-id 라는 Key값에 aws_vpc.this.id라는 값을 Value에 넣어주자.

output "pub-sub1-id" {
    value = aws_subnet.pub_sub1.id
}

output "pub-sub2-id" {
    value = aws_subnet.pub_sub2.id
}

output "prv-sub2-id" {
    value = aws_subnet.prv_sub2.id
}

output "prv-sub1-id" {
    value = aws_subnet.prv_sub1.id
}