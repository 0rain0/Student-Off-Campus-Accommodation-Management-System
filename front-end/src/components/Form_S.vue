<template>
        <table>
            <tr>
                <th colspan="8" class="center"><h1>校外賃居訪視記錄-教師填寫</h1></th>
            </tr>
            <tr>
                <th>系級：</th>
                <td><input type="text" class="underline-input" name="DG" :value="student.DG"></td>
                <th>學號：</th>
                <td><input type="text" class="underline-input" name="SID" :value="student.SID"></td>
                <th>姓名：</th>
                <td><input type="text" class="underline-input" name="S_Name" :value="student.S_Name"></td>
                <th>聯絡電話：</th>
                <td><input type="text" class="underline-input" name="S_Tel" :value="student.S_Tel"></td>
            </tr>
            <tr>
                <th>導師：</th>
                <td><input type="text" class="underline-input" name="T_Name" :value="student.T_Name"></td>
                <th>訪視時間：</th>
                <td colspan="5">
                    <input type="text" name="year" size="1" :value="new Date(student.V_Time).getFullYear()">年
                    <input type="text" name="month" size="1" :value="new Date(student.V_Time).getMonth() + 1">月
                    <input type="text" name="day" size="1" :value="new Date(student.V_Time).getDate()">日
                    <input type="text" name="hour" size="1" :value="new Date(student.V_Time).getHours()">時
                </td>
            </tr>
        </table>

        <table>
            <tr>
                <th colspan="6" class="line">校外賃居資料（學生填寫）</th>
            </tr>
            <tr>
                <th>房東姓名：</th>
                <td><input type="text" class="underline-input" name="L_Name" :value="student.L_Name"></td>
                <th>房東電話：</th>
                <td><input type="text" class="underline-input" name="L_Tel" :value="student.L_Tel"></td>
                <th>租賃地址：</th>
                <td colspan="3"><input type="text" class="underline-input" name="R_Addr" :value="student.R_Addr"></td>
            </tr>
            <tr>
                <th>室友姓名：</th>
                <td><input type="text" class="underline-input" name="RoommateN" :value="student.RoommateN"></td>
                <th>室友電話：</th>
                <td><input type="text" class="underline-input" name="RoommateP" :value="student.RoommateP"></td>
                <th>屋齡：</th>
                <td colspan="3"><input type="text" class="underline-input" name="RA" :value="student.RA"></td>
            </tr>
            <tr>
                <th>租屋型態：</th>
                <td colspan="3">
                    <div class="radio-group">
                        <label><input type="radio" name="RentType" value="0" :checked="student.RentType === 0"> 獨棟透天</label>
                        <label><input type="radio" name="RentType" value="1" :checked="student.RentType === 1"> 公寓(五樓以下)</label>
                        <label><input type="radio" name="RentType" value="2" :checked="student.RentType === 2"> 大樓(六樓以上)</label>
                        <label><input type="radio" name="RentType" value="3" :checked="student.RentType === 3"> 大型學舍(為學生建設的宿舍)</label>
                    </div>
                </td>
                <th>房間類型：</th>
                <td colspan="3">
                    <div class="radio-group">
                        <label><input type="radio" name="RoomType" value="0" :checked="student.RoomType === 0"> 套房</label>
                        <label><input type="radio" name="RoomType" value="1" :checked="student.RoomType === 1"> 雅房</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>每月租金：</th>
                <td><input type="text" class="underline-input" name="Price" :value="student.Price"></td>
                <th>押金：</th>
                <td><input type="text" class="underline-input" name="Deposit" :value="student.Deposit"></td>
                <th>是否值得推薦其他同學租賃：</th>
                <td colspan="3">
                    <div class="radio-group">
                        <label><input type="radio" name="Recommend" value="0" :checked="student.Recommend === 0"> 是</label>
                        <label><input type="radio" name="Recommend" value="1" :checked="student.Recommend === 1"> 否</label>
                    </div>
                </td>
            </tr>
        </table>

        <table>
            <tr>
                <th colspan="4" class="line">賃居安全自主管理檢視資料（學生填寫）</th>
            </tr>
            <tr>
                <th>木造隔間或鐵皮加蓋</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_01" value="0" :checked="student.SA_01 === 0"> 是</label>
                        <label><input type="radio" name="SA_01" value="1" :checked="student.SA_01 === 1"> 否</label>
                    </div>
                </td>
                <th>使用多種電器（高耗能）是否同時插在同一條延長線</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_02" value="0" :checked="student.SA_02 === 0"> 是</label>
                        <label><input type="radio" name="SA_02" value="1" :checked="student.SA_02 === 1"> 否</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>有火警警報器或偵煙器</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_03" value="0" :checked="student.SA_03 === 0"> 是</label>
                        <label><input type="radio" name="SA_03" value="1" :checked="student.SA_03 === 1"> 否</label>
                    </div>
                </td>
                <th>有滅火器且功能正常</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_04" value="0" :checked="student.SA_04 === 0"> 是</label>
                        <label><input type="radio" name="SA_04" value="1" :checked="student.SA_04 === 1"> 否</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>逃生通道暢通且標示清楚</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_05" value="0" :checked="student.SA_05 === 0"> 是</label>
                        <label><input type="radio" name="SA_05" value="1" :checked="student.SA_05 === 1"> 否</label>
                    </div>
                </td>
                <th>熱水器（電熱式及瓦斯式）安全良好，無一氧化碳中毒疑慮</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_06" value="0" :checked="student.SA_06 === 0"> 是</label>
                        <label><input type="radio" name="SA_06" value="1" :checked="student.SA_06 === 1"> 否</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>門禁及鎖具良好管理</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_07" value="0" :checked="student.SA_07 === 0"> 是</label>
                        <label><input type="radio" name="SA_07" value="1" :checked="student.SA_07 === 1"> 否</label>
                    </div>
                </td>
                <th>分間6個以上房間或10個以上床位</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_08" value="0" :checked="student.SA_08 === 0"> 是</label>
                        <label><input type="radio" name="SA_08" value="1" :checked="student.SA_08 === 1"> 否</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>有安裝照明設備（停車場及周遭）</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_09" value="0" :checked="student.SA_09 === 0"> 是</label>
                        <label><input type="radio" name="SA_09" value="1" :checked="student.SA_09 === 1"> 否</label>
                    </div>
                </td>
                <th>有安裝監視器設備</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_10" value="0" :checked="student.SA_10 === 0"> 是</label>
                        <label><input type="radio" name="SA_10" value="1" :checked="student.SA_10 === 1"> 否</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>瞭解熟悉電路安全及逃生要領</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_11" value="0" :checked="student.SA_11 === 0"> 是</label>
                        <label><input type="radio" name="SA_11" value="1" :checked="student.SA_11 === 1"> 否</label>
                    </div>
                </td>
                <th>使用<內政部定型化租賃契約></th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_12" value="0" :checked="student.SA_12 === 0"> 是</label>
                        <label><input type="radio" name="SA_12" value="1" :checked="student.SA_12 === 1"> 否</label>
                    </div>
                </td>
            </tr>
            <tr>
                <th>熟悉派出所、醫療、消防隊、學校校安專線電話</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="SA_13" value="0" :checked="student.SA_13 === 0"> 是</label>
                        <label><input type="radio" name="SA_13" value="1" :checked="student.SA_13 === 1"> 否</label>
                    </div>
                </td>
            </tr>
        </table>

        <form action="http://127.0.0.1:5000/receive_form_t" method="POST">
                          <table style="display:none">
                            <tr>
                                <th>系級：</th>
                                <td><input type="text" class="underline-input" name="DG" :value="student.DG"></td>
                                <th>學號：</th>
                                <td><input type="text" class="underline-input" name="SID" :value="student.SID"></td>
                                <th>姓名：</th>
                                <td><input type="text" class="underline-input" name="S_Name" :value="student.S_Name"></td>
                                <th>聯絡電話：</th>
                                <td><input type="text" class="underline-input" name="S_Tel" :value="student.S_Tel"></td>
                            </tr>
                            <tr>
                                <th>導師：</th>
                                <td><input type="text" class="underline-input" name="T_Name" :value="student.T_Name"></td>
                                <th>訪視時間：</th>
                                <td colspan="5">
                                    <input type="text" name="year" size="1" :value="new Date(student.V_Time).getFullYear()">年
                                    <input type="text" name="month" size="1" :value="new Date(student.V_Time).getMonth() + 1">月
                                    <input type="text" name="day" size="1" :value="new Date(student.V_Time).getDate()">日
                                    <input type="text" name="hour" size="1" :value="new Date(student.V_Time).getHours()">時
                                </td>
                            </tr>
                          </table>

                        <table style="display:none">
                            <tr>
                                <th colspan="6" class="line">校外賃居資料（學生填寫）</th>
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

                        <table>
                            <tr>
                                <th colspan="2" class="line">環境及作息評估（導師填寫）</th>
                            </tr>
                            <tr>
                                <th class="evaluate">押金要求</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="EN_01" value="0"> 合理</label>
                                        <label><input type="radio" name="EN_01" value="1"> 不合理（2個月以上之租金）</label>
                                    </div>
                                </td>
                            </tr>

                            <tr>
                                <th class="evaluate">水電費要求</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="EN_02" value="0"> 合理</label>
                                        <label><input type="radio" name="EN_02" value="1"> 不合理</label>
                                    </div>
                                </td>
                            </tr>

                            <tr>
                                <th class="evaluate">居住環境</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="EN_03" value="0"> 佳</label>
                                        <label><input type="radio" name="EN_03" value="1"> 適中</label>
                                        <label><input type="radio" name="EN_03" value="2"> 欠佳，說明：<input type="text" name="EN_03_Des" size="20"></label>
                                    </div>
                                </td>
                            </tr>

                            <tr>
                                <th class="evaluate">生活設施</th>
                                <td>
                                    <div class="radio-group">
                                        <label><input type="radio" name="EN_04" value="0"> 佳</label>
                                        <label><input type="radio" name="EN_04" value="1"> 適中</label>
                                        <label><input type="radio" name="EN_04" value="2"> 欠佳，說明：<input type="text" name="EN_04_Des" size="20"></label>
                                    </div>
                                </td>
                            </tr>

                            <tr>
                                <th class="evaluate">訪視現況</th>
                                <td colspan="3">
                                    <div class="radio-group">
                                        <label><input type="radio" name="VI_01" value="0"> 生活規律</label>
                                        <label><input type="radio" name="VI_01" value="1"> 適中</label>
                                        <label><input type="radio" name="VI_01" value="2"> 待加強，說明：<input type="text" name="VI_01_Des" size="20"></label>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <th class="evaluate">主客相處</th>
                                <td colspan="3">
                                    <div class="radio-group">
                                        <label><input type="radio" name="VI_02" value="0"> 和睦</label>
                                        <label><input type="radio" name="VI_02" value="1"> 欠佳</label>
                                    </div>
                                </td>
                            </tr>
                        </table>

                        <table>
                            <tr>
                                <th colspan="4" class="line">訪視結果（導師填寫）</th>
                            </tr>
                            <tr>
                                <th colspan="4">
                                    <div class="radio-group">
                                        <label><input type="radio" name="Result" value="0"> 整體賃居狀況良好</label>
                                        <label><input type="radio" name="Result" value="1"> 聯繫家長關注</label>
                                        <label><input type="radio" name="Result" value="2"> 安全堪慮請協助</label>
                                        <label><input type="radio" name="Result" value="3"> 其他，說明：<input type="text" name="RE_Des" size="20"></label>
                                    </div>
                                </th>
                            </tr>
                            <tr>
                                <th colspan="4">其他記載或建議事項：<input type="text" size="20" name="RE_Memo"></th>
                            </tr>

                            <tr>
                                <th colspan="4" class="line">關懷宣導項目（懇請導師賃居訪視時多予關懷叮嚀）</th>
                            </tr>
                            <tr>
                                <td colspan="4">
                                    <div class="radio-group">
                                        <label><input type="checkbox" name="DI_01" value="0"> 交通安全</label>
                                        <label><input type="checkbox" name="DI_02" value="0"> 拒絕菸害</label>
                                        <label><input type="checkbox" name="DI_03" value="0"> 拒絕毒品</label>
                                        <label><input type="checkbox" name="DI_04" value="0"> 登革熱防治</label>
                                        <label><input type="checkbox" name="DI_05" value="0"> 其他，說明：<input type="text" name="DI_05_Des" size="20"></label>
                                    </div>
                                </td>
                            </tr>
                        </table>
          <div align="center">
                <br>
                <input type="reset" value="清除表單" name="reset" class="styled-button">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <input type="submit" value="提交表單" name="submit" class="styled-button">
          </div>
        </form>
</template>

<script setup lang="ts">
import { defineProps, watch } from 'vue'

const props = defineProps({
    student: {
        type: Object,
        required: true
    }
})
watch(props.student, (newVal) => {
    console.log('Received student data in Form_S:', newVal)
})
</script>