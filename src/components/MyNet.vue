<template>
    <div id="left">
      <br/><br/><br/>
        <el-upload
          v-model:file-list="fileList"
          action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-remove="handleRemove"
          @click="myClick"
        >
          <el-icon><Plus /></el-icon>
        </el-upload>

        <el-dialog v-model="dialogVisible">
          <img w-full :src="dialogImageUrl" alt="Preview Image" />
        </el-dialog>
    <br/>
    <div><font size="4pt" color=" #3375b9">手动上传图片(不要超过1MB)</font></div>

    <br/><br/><br/>
    <el-input v-model="input" style="width:50%;" placeholder="输入随机数，从后台随机挑选一张图片" />

    <br/><br/><br/>
    <el-button color="#626aef" :dark="isDark" style="width:34%;" @click="random">电脑随机(5w以内整数)</el-button>
    <el-button type="danger" style="width:15%;" @click="getmethod">确定</el-button>

    </div>
    <div id="right">

      <el-empty v-if="label=='default'" :image-size="250" :description="label" style="width: 40%;"/>
      <br/><br/>
      <div v-if="label!='default'">
      <img :src="img_url" style="width:40%; float:left;" />
      <br/><br/>
      <div :src="label" v-if="label!='default'" ><font size="6pt" color=" #3375b9" > {{label}} </font> </div>
      <br/><br/>
      <font size="6pt" color=" #3375b9" >
      预测类别为：{{ pred_label }} 
      <br/><br/>
      置信度: {{probabilty}} </font>
      </div>
    
    </div>

</template>



<script>
import axios from "axios"

export default {
  name: "MyNet",
  data() {
    return {
      input: "",
      pred_label: "",
      label: "default",
      probabilty: "",
      img_url: "",
    };
  },
  
  methods: {
    random(){
        this.input = Math.floor(Math.random() * (50000));
    },
    getmethod(){
      axios.get('/api/predict/'+this.input, {responseType:"blob"}).then(res => {
        console.log(res);
        this.label = '数据集标签: '+res.headers.label;
        this.pred_label = res.headers.pred_label;
        this.probabilty = res.headers.prob;
        this.img_url = window.URL.createObjectURL(res.data);
      });
    },
    myClick(){
      alert("服务器配置较低，为了稳定运行，暂不开放用户图片上传功能，上传了也无效 : )");
    },
  },
};
</script>

<style>
#left{
  width: 50%;
  float:left;
  margin-left: 5%;
}

#right{
  width: 45%;
  float:right;
}

#right1{
  margin-top: 1%;
  height: 70%;
}

</style>