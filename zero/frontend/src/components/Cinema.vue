<template>
  <el-card class="box-card">
    <h3>试试</h3>
    <el-table :data="tableData">
      <el-table-column prop="name" label="影院列表" width="180"></el-table-column>
      <el-table-column prop="address" label="地址" width="180"></el-table-column>
      <el-table-column prop="price" label="价格" width="180"></el-table-column>
      <el-table-column prop="" label="" width="180"></el-table-column>
    </el-table>
  </el-card>
</template>

<script>
export default {
  name: 'Cinema',
  data () {
    return {
      tableData: []
    }
  },
  methods: {
    getCinema (url, pageID) {
      this.$ajax.get(url, {params: {page: pageID}}).then(response => {
        this.tableData = response.data.results
      }).catch(error => {
        console.log(error)
      }
      )
    }
  },
  mounted () {
    this.getCinema('http://127.0.0.1:8000/main/api/Cinema/', 1)
  }
}
</script>
