<template>
                      <table style="display:none">
                            <tr>
                                <th colspan="6" class="line">校外賃居資料（老師填寫）</th>
                            </tr>
                            <tr>
                                <th>房東姓名：</th>
                                <td><input type="text" class="underline-input" name="L_Name"></td>
                                <th>房東電話：</th>
                                <td><input type="text" class="underline-input" name="L_Tel"></td>
                                <th>租賃地址：</th>
                                <td colspan="3"><input type="text" class="underline-input" name="R_Addr"></td>
                            </tr>
                            <tr>
                                <th>室友姓名：</th>
                                <td><input type="text" class="underline-input" name="RoommateN"></td>
                                <th>室友電話：</th>
                                <td><input type="text" class="underline-input" name="RoommateP"></td>
                                <th>屋齡：</th>
                                <td colspan="3"><input type="text" class="underline-input" name="RA"></td>
                            </tr>
                            <tr>
                                <th>租屋型態：</th>
                                <td colspan="3">
                                    <div class="radio-group">
                                        <label><input type="radio" name="RentType" value="0"> 獨棟透天</label>
                                        <label><input type="radio" name="RentType" value="1"> 公寓(五樓以下)</label>
                                        <label><input type="radio" name="RentType" value="2"> 大樓(六樓以上)</label>
                                        <label><input type="radio" name="RentType" value="3"> 大型學舍(為學生建設的宿舍)</label>
                                    </div>
                                </td>
                                <th>房間類型：</th>
                                <td colspan="3">
                                    <div class="radio-group">
                                        <label><input type="radio" name="RoomType" value="0"> 套房</label>
                                        <label><input type="radio" name="RoomType" value="1"> 雅房</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>每月租金：</th>
                                <td><input type="text" class="underline-input" name="Price"></td>
                                <th>押金：</th>
                                <td><input type="text" class="underline-input" name="Deposit"></td>
                                <th>是否值得推薦其他同學租賃：</th>
                                <td colspan="3">
                                    <div class="radio-group">
                                        <label><input type="radio" name="Recommend" value="0"> 是</label>
                                        <label><input type="radio" name="Recommend" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                      </table>

                      <table style="display:none">
                            <tr>
                                <th colspan="4" class="line">賃居安全自主管理檢視資料（學生填寫）</th>
                            </tr>
                            <tr>
                                <th>木造隔間或鐵皮加蓋</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_01" value="0"> 是</label>
                                        <label><input type="radio" name="SA_01" value="1"> 否</label>
                                    </div>
                                </td>
                                <th>使用多種電器（高耗能）是否同時插在同一條延長線</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_02" value="0"> 是</label>
                                        <label><input type="radio" name="SA_02" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>有火警警報器或偵煙器</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_03" value="0"> 是</label>
                                        <label><input type="radio" name="SA_03" value="1"> 否</label>
                                    </div>
                                </td>
                                <th>有滅火器且功能正常</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_04" value="0"> 是</label>
                                        <label><input type="radio" name="SA_04" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>逃生通道暢通且標示清楚</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_05" value="0"> 是</label>
                                        <label><input type="radio" name="SA_05" value="1"> 否</label>
                                    </div>
                                </td>
                                <th>熱水器（電熱式及瓦斯式）安全良好，無一氧化碳中毒疑慮</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_06" value="0"> 是</label>
                                        <label><input type="radio" name="SA_06" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>門禁及鎖具良好管理</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_07" value="0"> 是</label>
                                        <label><input type="radio" name="SA_07" value="1"> 否</label>
                                    </div>
                                </td>
                                <th>分間6個以上房間或10個以上床位</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_08" value="0"> 是</label>
                                        <label><input type="radio" name="SA_08" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>有安裝照明設備（停車場及周遭）</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_09" value="0"> 是</label>
                                        <label><input type="radio" name="SA_09" value="1"> 否</label>
                                    </div>
                                </td>
                                <th>有安裝監視器設備</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_10" value="0"> 是</label>
                                        <label><input type="radio" name="SA_10" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>瞭解熟悉電路安全及逃生要領</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_11" value="0"> 是</label>
                                        <label><input type="radio" name="SA_11" value="1"> 否</label>
                                    </div>
                                </td>
                                <th>使用<內政部定型化租賃契約></th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_12" value="0"> 是</label>
                                        <label><input type="radio" name="SA_12" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th>熟悉派出所、醫療、消防隊、學校校安專線電話</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="SA_13" value="0"> 是</label>
                                        <label><input type="radio" name="SA_13" value="1"> 否</label>
                                    </div>
                                </td>
                            </tr>
                      </table>

</template>
<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
    student: {
        type: Object,
        required: true
    }
})
</script>