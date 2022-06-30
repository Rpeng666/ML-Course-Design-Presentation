<template>
    <el-container>
        <el-aside width="200px">
            <br/><br/><br/><br/>
            <el-button type="danger" round v-on:click = "changeMode1">AutoEncoder</el-button>
            <br/><br/><br/><br/><br/>
            <el-button type="danger" round v-on:click = "changeMode2">Co-teaching</el-button>
        </el-aside>
        <el-main>
            <embed v-if="mode==1" src="img/encoder.svg" width="39%" height="90%"/>
            <embed v-if="mode==1" src="img/baseblock.svg" width="22%" height="90%"/>
            <embed v-if="mode==1" src="img/decoder.svg" width="39%" height="90%"/>

            <embed v-if="mode==2" src="img/co-teaching.svg" width="50%" height="40%"/>
            <embed v-if="mode==2" src="img/co.svg" width="50%" height="40%"/>
        </el-main>
    </el-container>
</template>

<script>

export default {
    name:"ModelDesign",
    data(){
        return {
           mode:1
        }
    },
    methods:{
        changeMode1(){
            this.mode=1;
        },
        changeMode2(){
            this.mode=2;
        }
    }
}
</script>

<style>

</style>