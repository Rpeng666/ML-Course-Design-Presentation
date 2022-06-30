<template>
  <div class="common-layout">
    <el-container>
      <el-header height="100%">
        <div>
          <font size="12pt" color="#66b1ff"> 机器学习课程设计展示 </font>
          <br />
          <font size="6pt" color="#CFD3DC">带噪声的图像分类</font>
        </div>
      </el-header>

      <el-divider border-style="dashed">Rpeng Ym Wwl Zjc Ysm Zyj</el-divider>

      <el-main>
        <div class="workspace">
          <br /><br />
          <el-row :gutter="40" justify="center">
            <el-col :span="5">
              <el-button v-on:click="changeMode1" type="primary" size="large" >PCA可视化</el-button>
            </el-col>
            <el-col :span="5">
              <el-button v-on:click="changeMode2" type="success" size="large" >网络设计</el-button>
            </el-col>
            <el-col :span="5">
              <el-button v-on:click="changeMode3" type="warning" size="large">模型效果</el-button>
            </el-col>
            <el-col :span="5">
            <a href="https://github.com/Rpeng666/ML-Course-Design" target="_blank"><el-button color="#626aef" :dark="isDark" plain size="large">仓库链接</el-button></a>
            </el-col>
          </el-row>

          <br /><br /><br />

          <el-empty v-if="mode == -1" color="#fcfcfd" description="什么也没有 :)" />
          <MyPca v-if="mode == 1"></MyPca>
          <ModelDesign v-if="mode == 2"></ModelDesign>
          <MyNet v-if="mode == 3"></MyNet>
        </div>
      </el-main>
    </el-container>
  </div>
</template>


<script>
import MyPca from "./MyPca.vue";
import MyNet from "./MyNet.vue";
import ModelDesign from "./ModelDesign.vue";

export default {
  name: "MyIndex",
  data() {
    return {
      mode: -1,
    };
  },
  methods: {
    changeMode1() {
      this.mode = 1;
    },
    changeMode2() {
      this.mode = 2;
    },
    changeMode3() {
      this.mode = 3;
    },
  },
  components: { MyPca, MyNet, ModelDesign },
};
</script>

<style>
a{text-decoration: none;}


</style>