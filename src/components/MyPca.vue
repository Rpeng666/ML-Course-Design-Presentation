<template>
  <div class="pca_image">
    <table align="center" width="80%">
        <tr>
            <td>
                <el-image style="width: 50%; height: 50%" fit="fill" src="./img/2d_pca.png" /><br/>
                <a href="pca/2d_pca.html" target="_blank" style="color: cornflowerblue;">三类标签二维可视化</a>
            </td>
            
            <td>
                <el-image style="width: 40%; height: 40%" fit="fill" src="./img/2d_4_pca.png" /><br/>
                <a href="pca/2d_4_pca.html" target="_blank" style="color: cornflowerblue;">四类标签的二维可视化</a>
            </td>
            
        </tr>
        <br/>
        <tr>
            <td >
                <el-image style="width: 50%; height: 50%" fit="fill" src="./img/3d_4_pca.png"  /><br/>
                <a href="pca/3d_4_pca.html" target="_blank" style="color: cornflowerblue;">四类标签的三维可视化</a>
            </td>

            <td >
                <el-image style="width: 30%; height: 30%" fit="fill" src="./img/3d_pca_train_test.png"  /><br/>
                <a href="pca/3d_pca_train_test.html" target="_blank" style="color: cornflowerblue;">训练集和测试集的某两类</a>
            </td>
        </tr>
    </table>
    
</div>
</template>

<script>
export default {
    name:'MyPca'
}
</script>

<style>
.pca_image{
    color :cornflowerblue;
    font-size:large;
}

</style>