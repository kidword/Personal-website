<template>
  <div class="main" style="padding: 15px">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="新房" name="first">
        <div class="app-container">
          <div style='margin:15px 15px 30px 15px' class="selectoption">
            <el-row :gutter="24">
              <el-col :span="6">
                <label> 名称： </label>
                <el-input v-model="input" size="mini" placeholder="请输入内容" style="width: 150px" />
              </el-col>
              <el-button size="mini" type="primary" style="float:right; margin-right:15px">检索</el-button>
            </el-row>
          </div>
          <el-table
            v-loading="listLoading"
            :data="list"
            element-loading-text="Loading"
            border
            fit
            highlight-current-row
          >
            <el-table-column align="center" label="编号" width="90">
              <template slot-scope="scope">
                {{ scope.$index }}
              </template>
            </el-table-column>
            <el-table-column align="center" label="名称">
              <template slot-scope="scope">
                {{ scope.row.name }}
              </template>
            </el-table-column>
            <el-table-column label="户型" width="110" align="center">
              <template slot-scope="scope">
                {{ scope.row.model }}
              </template>
            </el-table-column>
            <el-table-column label="面积" width="110" align="center">
              <template slot-scope="scope">
                <span>{{ scope.row.area }}</span>
              </template>
            </el-table-column>
            <el-table-column label="朝向" align="center" width="110">
              <template slot-scope="scope">
                {{ scope.row.toward }}
              </template>
            </el-table-column>
            <el-table-column class-name="status-col" label="装修" width="110" align="center">
              <template slot-scope="scope">
                <el-tag :type="scope.row.decorate | statusFilter">{{ scope.row.decorate }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column align="center" label="楼层">
              <template slot-scope="scope">
                <span>{{ scope.row.positionInfo }}</span>
              </template>
            </el-table-column>
            <el-table-column align="center" label="单价" width="100">
              <template slot-scope="scope">
                <span>{{ scope.row.price }}</span>
              </template>
            </el-table-column>
            <el-table-column align="center" label="总价" width="100">
              <template slot-scope="scope">
                <span>{{ scope.row.res_price }}</span>
              </template>
            </el-table-column>
            <el-table-column align="center" label="成交时间" width="150">
              <template slot-scope="scope">
                <i class="el-icon-time" /> &nbsp;
                <span>{{ scope.row.time }}</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-tab-pane>
      <el-tab-pane label="二手房" name="second" />
    </el-tabs>
  </div>

</template>

<script>
import { getList } from '@/api/table'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap.published
    }
  },
  data() {
    return {
      list: null,
      listLoading: true,
      activeName: 'first',
      input: ''
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList({ 'menu': '1' }).then(response => {
        this.list = response.data.items
        // console.log(response.data)
        this.listLoading = false
      })
    },
    handleClick(tab, event) {
      console.log(tab, event)
    }
  }
}
</script>

<style scoped>
.selectoption label{font-size: 14px; font-weight: 500;}

</style>
