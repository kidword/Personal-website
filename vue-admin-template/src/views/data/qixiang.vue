<template>
  <div class="main" style="padding: 15px">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="气象站预报" name="first">
        <div class="app-container">
          <el-table
            v-loading="listLoading"
            :data="forecast"
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
            <el-table-column align="center" label="名称" width="150">
              <template slot-scope="scope">
                {{ scope.row.name }}
              </template>
            </el-table-column>
            <el-table-column label="预报内容">
              <template slot-scope="scope">
                {{ scope.row.content }}
              </template>
            </el-table-column>
            <el-table-column label="类型" width="110" align="center">
              <template slot-scope="scope">
                <span>{{ scope.row.type }}</span>
              </template>
            </el-table-column>
            <el-table-column label="所在地" width="110" align="center">
              <template slot-scope="scope">
                {{ scope.row.location }}
              </template>
            </el-table-column>
            <el-table-column class-name="status-col" label="等级" width="110" align="center">
              <template slot-scope="scope">
                <el-tag :type="scope.row.level | statusFilter">{{ scope.row.level }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="created_at" label="Display_time" width="200">
              <template slot-scope="scope">
                <i class="el-icon-time" /> &nbsp;
                <span>{{ scope.row.display_time }}</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-tab-pane>
      <el-tab-pane label="气候" name="second" />
      <el-tab-pane label="三维闪电" name="third" />
      <el-tab-pane label="气象站" name="fourth" />
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
      if (status === '蓝色') {
        return statusMap.draft
      }
      if (status === '黄色') {
        return statusMap.published
      }
      if (status === '红色') {
        return statusMap.deleted
      } else {
        return statusMap.published
      }
    }
  },
  data() {
    return {
      forecast: null, // 气象站预报list
      listLoading: true,
      activeName: 'first'
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList({ 'menu': '1' }).then(response => {
        this.forecast = response.data.items
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
