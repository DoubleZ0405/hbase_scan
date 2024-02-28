# 基于cntos7，如果没有这个镜像那么它会下载这个镜像。
FROM centos:7
# 创建者(这个可以不写)
MAINTAINER whalexiao
# 为Dockerfile中所有RUN、CMD、ENTRYPOINT、COPY和ADD指令设定工作目录
WORKDIR /usr
# 执行命令(这里创建了一个目录)
# RUN mkdir /usr/local/java && \
RUN yum install -y java-1.8.0-openjdk.x86_64 && \
        yum install -y git
# 和copy一样，复制文件到指定目录，但是copy不能解压，add自动解压
ADD test.jar .
CMD ["java", "-jar", "test.jar"]
# 重命名(不知道文件名可以现在宿主机解压后看一下)
# RUN ln -s /usr/local/java/jdk1.8.0_181 /usr/local/java/jdk
# 设置环境变量 
# ENV JAVA_HOME /usr/local/java/jdk
#ENV JRE_HOME ${JAVA_HOME}/jre
#ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
#ENV PATH ${JAVA_HOME}/bin:$PATH
#ENV JAVA_HOME=/usr/lib/jvm/jre-1.6.0-openjdk.x86_64
#ENV PATH=$PATH:$JAVA_HOME/bin
#ENV CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar